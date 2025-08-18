#!/usr/bin/env python3
"""
Enhanced Confluence Content Extractor with Image Support
This script properly handles Confluence images and attachments
"""

import os
import re
import json
import requests
from pathlib import Path
from typing import Dict, List, Optional
import logging
from urllib.parse import urljoin

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class EnhancedConfluenceExtractor:
    """Enhanced extractor that properly handles images from Confluence"""
    
    def __init__(self, base_url: str = "https://bigledger.atlassian.net", 
                 space_key: str = "AKAUN",
                 username: str = None,
                 api_token: str = None):
        self.base_url = base_url
        self.space_key = space_key
        self.username = username
        self.api_token = api_token
        self.output_dir = Path("confluence_with_images")
        self.output_dir.mkdir(exist_ok=True)
        self.images_dir = self.output_dir / "images"
        self.images_dir.mkdir(exist_ok=True)
        
    def get_session(self):
        """Create authenticated session"""
        session = requests.Session()
        if self.username and self.api_token:
            session.auth = (self.username, self.api_token)
        session.headers.update({
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        })
        return session
    
    def get_pages(self, session, limit: int = 100):
        """Get all pages from space with expanded content"""
        url = f"{self.base_url}/wiki/rest/api/content"
        params = {
            'spaceKey': self.space_key,
            'type': 'page',
            'limit': limit,
            # Important: expand body.storage to get HTML content
            'expand': 'body.storage,metadata.labels,version,ancestors'
        }
        
        try:
            response = session.get(url, params=params)
            if response.status_code == 200:
                return response.json().get('results', [])
        except Exception as e:
            logger.error(f"Error fetching pages: {e}")
        return []
    
    def get_page_attachments(self, session, page_id: str):
        """Get all attachments for a page"""
        url = f"{self.base_url}/wiki/rest/api/content/{page_id}/child/attachment"
        params = {
            'expand': 'version,container',
            'limit': 100
        }
        
        try:
            response = session.get(url, params=params)
            if response.status_code == 200:
                return response.json().get('results', [])
        except Exception as e:
            logger.error(f"Error fetching attachments for page {page_id}: {e}")
        return []
    
    def download_attachment(self, session, attachment: Dict, page_title: str):
        """Download attachment and return local path"""
        try:
            # Create page-specific directory
            page_dir = self.images_dir / self.sanitize_filename(page_title)
            page_dir.mkdir(exist_ok=True)
            
            # Get download URL
            download_path = attachment['_links']['download']
            if not download_path.startswith('http'):
                download_url = self.base_url + download_path
            else:
                download_url = download_path
            
            # Download file
            response = session.get(download_url, stream=True)
            if response.status_code == 200:
                filename = attachment['title']
                local_path = page_dir / filename
                
                with open(local_path, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                
                logger.info(f"  Downloaded: {filename}")
                # Return relative path for markdown
                return f"images/{self.sanitize_filename(page_title)}/{filename}"
        except Exception as e:
            logger.error(f"Error downloading attachment: {e}")
        return None
    
    def convert_confluence_to_markdown(self, html_content: str, attachments: Dict[str, str]):
        """Convert Confluence HTML to Markdown with proper image handling"""
        
        # First, convert Confluence image macros to standard HTML
        # Pattern: <ac:image><ri:attachment ri:filename="image.png"/></ac:image>
        def replace_confluence_image(match):
            filename = match.group(1)
            if filename in attachments:
                local_path = attachments[filename]
                return f'![{filename}]({local_path})'
            return f'![{filename}](missing-image:{filename})'
        
        # Replace Confluence image macros
        content = re.sub(
            r'<ac:image[^>]*>.*?<ri:attachment\s+ri:filename="([^"]+)".*?</ac:image>',
            replace_confluence_image,
            html_content,
            flags=re.DOTALL
        )
        
        # Also handle inline images with ac:inline-image
        content = re.sub(
            r'<ac:inline-image[^>]*>.*?<ri:attachment\s+ri:filename="([^"]+)".*?</ac:inline-image>',
            replace_confluence_image,
            content,
            flags=re.DOTALL
        )
        
        # Now convert to markdown using html2text
        try:
            import html2text
            h2t = html2text.HTML2Text()
            h2t.body_width = 0
            h2t.ignore_links = False
            h2t.ignore_images = False  # Important: don't ignore images
            
            markdown = h2t.handle(content)
            
            # Clean up remaining Confluence-specific tags
            markdown = re.sub(r'<ac:.*?>', '', markdown)
            markdown = re.sub(r'</ac:.*?>', '', markdown)
            markdown = re.sub(r'<ri:.*?/>', '', markdown)
            
            return markdown
        except ImportError:
            logger.error("html2text not installed. Run: pip install html2text")
            return content
    
    def sanitize_filename(self, filename: str) -> str:
        """Sanitize filename for filesystem"""
        # Replace problematic characters
        filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
        filename = filename.strip()
        return filename[:100]  # Limit length
    
    def process_page(self, session, page: Dict):
        """Process a single page with its attachments"""
        page_title = page['title']
        page_id = page['id']
        
        logger.info(f"Processing: {page_title}")
        
        # Get attachments
        attachments_list = self.get_page_attachments(session, page_id)
        attachments_map = {}
        
        if attachments_list:
            logger.info(f"  Found {len(attachments_list)} attachments")
            for attachment in attachments_list:
                local_path = self.download_attachment(session, attachment, page_title)
                if local_path:
                    attachments_map[attachment['title']] = local_path
        
        # Get HTML content
        html_content = ""
        if 'body' in page and 'storage' in page['body']:
            html_content = page['body']['storage'].get('value', '')
        
        # Convert to markdown with images
        markdown_content = self.convert_confluence_to_markdown(html_content, attachments_map)
        
        # Add metadata
        full_content = f"# {page_title}\n\n"
        full_content += f"**Page ID**: {page_id}\n"
        if 'version' in page and 'when' in page['version']:
            full_content += f"**Last Updated**: {page['version']['when']}\n"
        full_content += "\n---\n\n"
        full_content += markdown_content
        
        # Add attachments list if any
        if attachments_map:
            full_content += "\n\n## Attachments\n\n"
            for filename, path in attachments_map.items():
                full_content += f"- [{filename}]({path})\n"
        
        # Save markdown file
        output_file = self.output_dir / f"{self.sanitize_filename(page_title)}.md"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(full_content)
        
        return {
            'title': page_title,
            'file': str(output_file),
            'attachments': len(attachments_map),
            'has_images': len(attachments_map) > 0
        }
    
    def extract_all(self):
        """Main extraction process"""
        logger.info(f"Starting extraction from {self.base_url}/wiki/spaces/{self.space_key}")
        
        session = self.get_session()
        pages = self.get_pages(session)
        
        if not pages:
            logger.error("No pages found or authentication failed")
            return
        
        logger.info(f"Found {len(pages)} pages to process")
        
        results = []
        for page in pages:
            result = self.process_page(session, page)
            results.append(result)
        
        # Generate summary
        total_pages = len(results)
        pages_with_images = sum(1 for r in results if r['has_images'])
        total_attachments = sum(r['attachments'] for r in results)
        
        summary = {
            'total_pages': total_pages,
            'pages_with_images': pages_with_images,
            'total_attachments': total_attachments,
            'output_directory': str(self.output_dir),
            'pages': results
        }
        
        # Save summary
        with open(self.output_dir / 'extraction_summary.json', 'w') as f:
            json.dump(summary, f, indent=2)
        
        logger.info(f"\nExtraction Complete!")
        logger.info(f"Total Pages: {total_pages}")
        logger.info(f"Pages with Images: {pages_with_images}")
        logger.info(f"Total Attachments: {total_attachments}")
        logger.info(f"Output Directory: {self.output_dir}")
        
        return summary

def main():
    """Main entry point"""
    # Check for credentials
    username = os.environ.get('CONFLUENCE_USERNAME')
    api_token = os.environ.get('CONFLUENCE_API_TOKEN')
    
    if not username or not api_token:
        logger.warning("No credentials found. Attempting anonymous access...")
        logger.info("For authenticated access, set environment variables:")
        logger.info("  export CONFLUENCE_USERNAME='your-email@example.com'")
        logger.info("  export CONFLUENCE_API_TOKEN='your-api-token'")
    
    extractor = EnhancedConfluenceExtractor(
        username=username,
        api_token=api_token
    )
    
    extractor.extract_all()

if __name__ == "__main__":
    main()