#!/usr/bin/env python3
"""
Authenticated Confluence Content Extractor
Uses Atlassian API with authentication for full access
"""

import os
import re
import json
import base64
from pathlib import Path
from typing import Dict, List, Optional
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class AuthenticatedConfluenceExtractor:
    """Extract Confluence content using authentication"""
    
    def __init__(self, 
                 base_url: str = "https://bigledger.atlassian.net",
                 username: str = None,
                 api_token: str = None,
                 space_key: str = "AKAUN"):
        """
        Initialize with authentication credentials
        
        Args:
            base_url: Confluence base URL
            username: Your Atlassian email
            api_token: Your Atlassian API token (get from https://id.atlassian.com/manage/api-tokens)
            space_key: The space key to extract
        """
        self.base_url = base_url
        self.space_key = space_key
        self.username = username or os.getenv('ATLASSIAN_USERNAME')
        self.api_token = api_token or os.getenv('ATLASSIAN_API_TOKEN')
        
        # Setup output directory
        self.output_dir = Path("tmp/confluence_content")
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Check for credentials
        if not self.username or not self.api_token:
            logger.warning("No credentials provided. Set ATLASSIAN_USERNAME and ATLASSIAN_API_TOKEN environment variables or pass them directly.")
            logger.info("Get your API token from: https://id.atlassian.com/manage/api-tokens")
        
    def setup_session(self):
        """Setup authenticated session"""
        try:
            import requests
            from requests.auth import HTTPBasicAuth
            
            session = requests.Session()
            
            # Use basic auth with API token
            session.auth = HTTPBasicAuth(self.username, self.api_token)
            
            # Set headers
            session.headers.update({
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            })
            
            return session
            
        except ImportError:
            logger.error("requests library not installed. Run: pip install requests")
            return None
    
    def test_authentication(self, session) -> bool:
        """Test if authentication works"""
        url = f"{self.base_url}/wiki/rest/api/user/current"
        
        try:
            response = session.get(url)
            if response.status_code == 200:
                user_data = response.json()
                logger.info(f"✓ Authenticated as: {user_data.get('displayName', 'Unknown')}")
                return True
            else:
                logger.error(f"✗ Authentication failed: {response.status_code}")
                return False
        except Exception as e:
            logger.error(f"✗ Authentication error: {e}")
            return False
    
    def get_all_spaces(self, session) -> List[Dict]:
        """Get all accessible spaces"""
        url = f"{self.base_url}/wiki/rest/api/space"
        spaces = []
        
        params = {
            'limit': 100,
            'expand': 'description.plain,homepage'
        }
        
        while url:
            try:
                response = session.get(url, params=params)
                if response.status_code == 200:
                    data = response.json()
                    spaces.extend(data.get('results', []))
                    
                    # Check for next page
                    if '_links' in data and 'next' in data['_links']:
                        url = self.base_url + data['_links']['next']
                        params = {}  # URL already has params
                    else:
                        url = None
                else:
                    logger.error(f"Failed to get spaces: {response.status_code}")
                    break
                    
            except Exception as e:
                logger.error(f"Error getting spaces: {e}")
                break
        
        return spaces
    
    def get_space_content(self, session, space_key: str = None) -> List[Dict]:
        """Get all pages in a space"""
        space_key = space_key or self.space_key
        url = f"{self.base_url}/wiki/rest/api/content"
        
        pages = []
        params = {
            'spaceKey': space_key,
            'type': 'page',
            'expand': 'body.storage,body.view,metadata.labels,version,ancestors,children.page',
            'limit': 100
        }
        
        while url:
            try:
                response = session.get(url, params=params)
                if response.status_code == 200:
                    data = response.json()
                    pages.extend(data.get('results', []))
                    
                    logger.info(f"Fetched {len(data.get('results', []))} pages, total: {len(pages)}")
                    
                    # Check for next page
                    if '_links' in data and 'next' in data['_links']:
                        url = self.base_url + data['_links']['next']
                        params = {}
                    else:
                        url = None
                else:
                    logger.error(f"Failed to get content: {response.status_code}")
                    logger.error(response.text)
                    break
                    
            except Exception as e:
                logger.error(f"Error getting content: {e}")
                break
        
        return pages
    
    def get_page_attachments(self, session, page_id: str) -> List[Dict]:
        """Get attachments for a page"""
        url = f"{self.base_url}/wiki/rest/api/content/{page_id}/child/attachment"
        
        try:
            response = session.get(url)
            if response.status_code == 200:
                data = response.json()
                return data.get('results', [])
        except Exception as e:
            logger.error(f"Error getting attachments: {e}")
        
        return []
    
    def download_attachment(self, session, attachment: Dict, output_dir: Path):
        """Download an attachment"""
        try:
            download_url = self.base_url + attachment['_links']['download']
            response = session.get(download_url, stream=True)
            
            if response.status_code == 200:
                filename = output_dir / attachment['title']
                with open(filename, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                logger.info(f"  Downloaded: {attachment['title']}")
                return True
        except Exception as e:
            logger.error(f"  Failed to download {attachment['title']}: {e}")
        
        return False
    
    def convert_to_markdown(self, html_content: str) -> str:
        """Convert Confluence storage format to Markdown"""
        try:
            import html2text
            
            h2t = html2text.HTML2Text()
            h2t.body_width = 0
            h2t.ignore_links = False
            
            # Convert to markdown
            markdown = h2t.handle(html_content)
            
            # Clean up Confluence-specific elements
            markdown = re.sub(r'<ac:.*?>', '', markdown)
            markdown = re.sub(r'</ac:.*?>', '', markdown)
            markdown = re.sub(r'<ri:.*?/>', '', markdown)
            
            return markdown
            
        except ImportError:
            logger.error("html2text not installed. Run: pip install html2text")
            return html_content
    
    def save_page(self, page: Dict, category: str = "general"):
        """Save a page to disk"""
        # Create category directory
        category_dir = self.output_dir / category
        category_dir.mkdir(exist_ok=True)
        
        # Get page details
        title = page.get('title', 'untitled')
        page_id = page.get('id', 'unknown')
        
        # Create safe filename
        safe_title = re.sub(r'[^a-zA-Z0-9\s\-_]', '', title)
        safe_title = safe_title.replace(' ', '_')[:100]
        
        # Get content
        content_html = ""
        if 'body' in page:
            if 'storage' in page['body']:
                content_html = page['body']['storage'].get('value', '')
            elif 'view' in page['body']:
                content_html = page['body']['view'].get('value', '')
        
        # Convert to markdown
        markdown_content = self.convert_to_markdown(content_html)
        
        # Add metadata header
        metadata = f"""---
title: {title}
confluence_id: {page_id}
confluence_url: {self.base_url}/wiki/spaces/{self.space_key}/pages/{page_id}
last_updated: {page.get('version', {}).get('when', 'unknown')}
---

# {title}

"""
        
        # Save markdown file
        md_filename = category_dir / f"{safe_title}.md"
        with open(md_filename, 'w', encoding='utf-8') as f:
            f.write(metadata + markdown_content)
        
        # Save original HTML
        html_filename = category_dir / f"{safe_title}.html"
        with open(html_filename, 'w', encoding='utf-8') as f:
            f.write(content_html)
        
        # Save metadata
        meta_filename = category_dir / f"{safe_title}_meta.json"
        with open(meta_filename, 'w', encoding='utf-8') as f:
            json.dump({
                'id': page_id,
                'title': title,
                'type': page.get('type'),
                'status': page.get('status'),
                'version': page.get('version'),
                'ancestors': page.get('ancestors', []),
                'labels': page.get('metadata', {}).get('labels', {}).get('results', [])
            }, f, indent=2)
        
        logger.info(f"Saved: {title}")
        
        return md_filename
    
    def categorize_page(self, page: Dict) -> str:
        """Categorize page based on title and labels"""
        title = page.get('title', '').lower()
        labels = [l.get('name', '') for l in page.get('metadata', {}).get('labels', {}).get('results', [])]
        labels_str = ' '.join(labels).lower()
        
        # Check title and labels for keywords
        if any(word in title + labels_str for word in ['account', 'finance', 'ledger', 'journal']):
            return 'accounting'
        elif any(word in title + labels_str for word in ['invoice', 'einvoice', 'e-invoice', 'peppol']):
            return 'einvoice'
        elif any(word in title + labels_str for word in ['stock', 'inventory', 'warehouse']):
            return 'inventory'
        elif any(word in title + labels_str for word in ['sales', 'pos', 'customer']):
            return 'sales'
        elif any(word in title + labels_str for word in ['purchase', 'vendor', 'supplier']):
            return 'purchasing'
        elif any(word in title + labels_str for word in ['api', 'integration', 'webhook']):
            return 'api'
        elif any(word in title + labels_str for word in ['guide', 'tutorial', 'how-to']):
            return 'guides'
        elif any(word in title + labels_str for word in ['setup', 'config', 'install']):
            return 'setup'
        else:
            return 'general'
    
    def extract_all_content(self):
        """Main extraction process"""
        logger.info("=" * 60)
        logger.info("Authenticated Confluence Content Extraction")
        logger.info("=" * 60)
        
        # Check credentials
        if not self.username or not self.api_token:
            logger.error("\n⚠️  No credentials provided!")
            logger.info("\nTo use this extractor:")
            logger.info("1. Get your API token from: https://id.atlassian.com/manage/api-tokens")
            logger.info("2. Set environment variables:")
            logger.info("   export ATLASSIAN_USERNAME='your-email@example.com'")
            logger.info("   export ATLASSIAN_API_TOKEN='your-api-token'")
            logger.info("\nOr pass them directly to the script")
            return None
        
        # Setup session
        session = self.setup_session()
        if not session:
            return None
        
        # Test authentication
        if not self.test_authentication(session):
            logger.error("Authentication failed. Check your credentials.")
            return None
        
        # Get all spaces
        logger.info("\nFetching available spaces...")
        spaces = self.get_all_spaces(session)
        logger.info(f"Found {len(spaces)} spaces")
        
        # List spaces
        for space in spaces[:10]:  # Show first 10
            logger.info(f"  - {space.get('key')}: {space.get('name')}")
        
        # Get content from target space
        logger.info(f"\nExtracting content from space: {self.space_key}")
        pages = self.get_space_content(session)
        logger.info(f"Found {len(pages)} pages")
        
        if not pages:
            logger.warning("No pages found. Check the space key or permissions.")
            return None
        
        # Organize and save pages
        categorized = {}
        for page in pages:
            category = self.categorize_page(page)
            if category not in categorized:
                categorized[category] = []
            categorized[category].append(page)
        
        # Save pages by category
        saved_files = []
        for category, category_pages in categorized.items():
            logger.info(f"\nSaving {len(category_pages)} pages in category: {category}")
            for page in category_pages:
                saved_file = self.save_page(page, category)
                saved_files.append(saved_file)
                
                # Check for attachments
                attachments = self.get_page_attachments(session, page['id'])
                if attachments:
                    logger.info(f"  Found {len(attachments)} attachments")
                    attachments_dir = self.output_dir / category / "attachments"
                    attachments_dir.mkdir(exist_ok=True)
                    
                    for attachment in attachments:
                        self.download_attachment(session, attachment, attachments_dir)
        
        # Generate summary report
        self.generate_report(categorized, saved_files)
        
        return saved_files
    
    def generate_report(self, categorized: Dict, saved_files: List):
        """Generate extraction report"""
        report = f"""# Confluence Extraction Report

**Date**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Space**: {self.space_key}
**Total Pages**: {sum(len(pages) for pages in categorized.values())}

## Content by Category

"""
        
        for category, pages in categorized.items():
            report += f"### {category.title()} ({len(pages)} pages)\n\n"
            for page in pages[:5]:  # Show first 5
                report += f"- {page.get('title')}\n"
            if len(pages) > 5:
                report += f"- ... and {len(pages) - 5} more\n"
            report += "\n"
        
        report += f"""
## Next Steps

1. Review extracted content in: {self.output_dir}
2. Convert relevant content to documentation
3. Update BigLedger wiki with new content

## Files Saved

Total files: {len(saved_files)}
Location: {self.output_dir}
"""
        
        # Save report
        report_file = self.output_dir / "extraction_report.md"
        with open(report_file, 'w') as f:
            f.write(report)
        
        logger.info(f"\n{'=' * 60}")
        logger.info(f"Extraction complete!")
        logger.info(f"Report saved to: {report_file}")
        logger.info(f"Content saved to: {self.output_dir}")


def main():
    """Main execution"""
    
    # You can pass credentials here or use environment variables
    username = input("Enter your Atlassian email (or press Enter to use env var): ").strip()
    api_token = input("Enter your API token (or press Enter to use env var): ").strip()
    space_key = input("Enter space key (default: AKAUN): ").strip() or "AKAUN"
    
    if not username:
        username = None  # Will use env var
    if not api_token:
        api_token = None  # Will use env var
    
    # Create extractor
    extractor = AuthenticatedConfluenceExtractor(
        username=username,
        api_token=api_token,
        space_key=space_key
    )
    
    # Extract content
    saved_files = extractor.extract_all_content()
    
    if saved_files:
        logger.info(f"\n✓ Successfully extracted {len(saved_files)} pages")
    else:
        logger.info("\n✗ Extraction failed or no content found")
    
    return saved_files


if __name__ == "__main__":
    main()