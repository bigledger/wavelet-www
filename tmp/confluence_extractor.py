#!/usr/bin/env python3
"""
Confluence Content Extractor for BigLedger Documentation
Extracts content from BigLedger Confluence and converts to markdown
"""

import os
import re
import json
import time
import requests
from pathlib import Path
from typing import Dict, List, Optional
from urllib.parse import urlparse, urljoin
import html2text
from bs4 import BeautifulSoup
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class ConfluenceExtractor:
    """Extract content from Confluence spaces"""
    
    def __init__(self, base_url: str, space_key: str = "AKAUN", 
                 username: Optional[str] = None, password: Optional[str] = None):
        self.base_url = base_url
        self.space_key = space_key
        self.username = username
        self.password = password
        self.session = requests.Session()
        
        # Setup authentication if provided
        if username and password:
            self.session.auth = (username, password)
        
        # Configure html2text
        self.h2t = html2text.HTML2Text()
        self.h2t.ignore_links = False
        self.h2t.ignore_images = False
        self.h2t.body_width = 0
        self.h2t.protect_links = True
        
        # Create output directories
        self.output_dir = Path("extracted_content")
        self.output_dir.mkdir(exist_ok=True)
        
    def get_space_content(self) -> List[Dict]:
        """Get all pages in a Confluence space using REST API"""
        pages = []
        try:
            # Try REST API first
            api_url = f"{self.base_url}/rest/api/content"
            params = {
                'spaceKey': self.space_key,
                'type': 'page',
                'expand': 'body.storage,metadata.labels,ancestors',
                'limit': 100
            }
            
            while True:
                response = self.session.get(api_url, params=params)
                if response.status_code == 200:
                    data = response.json()
                    pages.extend(data.get('results', []))
                    
                    # Check for more pages
                    if 'next' in data.get('_links', {}):
                        api_url = urljoin(self.base_url, data['_links']['next'])
                        params = {}  # URL already has params
                    else:
                        break
                else:
                    logger.warning(f"API request failed with status {response.status_code}")
                    break
                    
        except Exception as e:
            logger.error(f"Error fetching space content: {e}")
            
        return pages
    
    def scrape_public_content(self) -> List[Dict]:
        """Fallback method to scrape public Confluence pages"""
        pages = []
        try:
            # Try to access the space overview page
            space_url = f"{self.base_url}/wiki/spaces/{self.space_key}/overview"
            response = self.session.get(space_url)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # Find all page links in the space
                page_links = soup.find_all('a', href=re.compile(f'/wiki/spaces/{self.space_key}/pages/'))
                
                for link in page_links:
                    page_url = urljoin(self.base_url, link.get('href'))
                    page_title = link.get_text(strip=True)
                    
                    # Extract page content
                    page_content = self.scrape_page(page_url)
                    if page_content:
                        pages.append({
                            'title': page_title,
                            'url': page_url,
                            'content': page_content
                        })
                        time.sleep(0.5)  # Be respectful with requests
                        
        except Exception as e:
            logger.error(f"Error scraping content: {e}")
            
        return pages
    
    def scrape_page(self, url: str) -> Optional[str]:
        """Scrape individual page content"""
        try:
            response = self.session.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # Try to find main content area (adjust selectors based on Confluence version)
                content_selectors = [
                    'div#main-content',
                    'div.wiki-content',
                    'article',
                    'div[data-testid="page-content"]'
                ]
                
                content = None
                for selector in content_selectors:
                    content = soup.select_one(selector)
                    if content:
                        break
                
                if content:
                    return str(content)
                    
        except Exception as e:
            logger.error(f"Error scraping page {url}: {e}")
            
        return None
    
    def convert_to_markdown(self, html_content: str, title: str = "") -> str:
        """Convert HTML content to Markdown"""
        try:
            # Clean up HTML before conversion
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # Remove script and style tags
            for tag in soup(['script', 'style']):
                tag.decompose()
            
            # Convert to markdown
            markdown = self.h2t.handle(str(soup))
            
            # Add title if provided
            if title:
                markdown = f"# {title}\n\n{markdown}"
            
            # Clean up excessive newlines
            markdown = re.sub(r'\n{3,}', '\n\n', markdown)
            
            return markdown
            
        except Exception as e:
            logger.error(f"Error converting to markdown: {e}")
            return ""
    
    def organize_content(self, pages: List[Dict]) -> Dict[str, List[Dict]]:
        """Organize pages by category/topic"""
        organized = {
            'accounting': [],
            'sales': [],
            'inventory': [],
            'purchasing': [],
            'einvoice': [],
            'reports': [],
            'setup': [],
            'guides': [],
            'api': [],
            'other': []
        }
        
        for page in pages:
            title_lower = page.get('title', '').lower()
            
            # Categorize based on title keywords
            if any(word in title_lower for word in ['account', 'ledger', 'journal', 'financial']):
                organized['accounting'].append(page)
            elif any(word in title_lower for word in ['sales', 'customer', 'invoice', 'pos']):
                organized['sales'].append(page)
            elif any(word in title_lower for word in ['stock', 'inventory', 'warehouse']):
                organized['inventory'].append(page)
            elif any(word in title_lower for word in ['purchase', 'vendor', 'supplier', 'procurement']):
                organized['purchasing'].append(page)
            elif any(word in title_lower for word in ['e-invoice', 'einvoice', 'peppol', 'myinvois']):
                organized['einvoice'].append(page)
            elif any(word in title_lower for word in ['report', 'analytics', 'dashboard']):
                organized['reports'].append(page)
            elif any(word in title_lower for word in ['setup', 'configuration', 'install']):
                organized['setup'].append(page)
            elif any(word in title_lower for word in ['guide', 'tutorial', 'how to', 'howto']):
                organized['guides'].append(page)
            elif any(word in title_lower for word in ['api', 'integration', 'webhook']):
                organized['api'].append(page)
            else:
                organized['other'].append(page)
        
        return organized
    
    def save_content(self, pages: List[Dict], category: str = "general"):
        """Save extracted content to files"""
        category_dir = self.output_dir / category
        category_dir.mkdir(exist_ok=True)
        
        for page in pages:
            # Create safe filename
            title = page.get('title', 'untitled')
            safe_title = re.sub(r'[^a-zA-Z0-9\s\-_]', '', title)
            safe_title = safe_title.replace(' ', '_')[:100]
            
            # Convert content to markdown
            if 'body' in page and 'storage' in page['body']:
                html_content = page['body']['storage'].get('value', '')
            else:
                html_content = page.get('content', '')
            
            markdown = self.convert_to_markdown(html_content, title)
            
            # Save markdown file
            filename = category_dir / f"{safe_title}.md"
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(markdown)
                
            # Save metadata
            metadata = {
                'title': title,
                'url': page.get('url', ''),
                'id': page.get('id', ''),
                'labels': page.get('metadata', {}).get('labels', {}).get('results', []),
                'ancestors': page.get('ancestors', [])
            }
            
            meta_filename = category_dir / f"{safe_title}_meta.json"
            with open(meta_filename, 'w', encoding='utf-8') as f:
                json.dump(metadata, f, indent=2)
            
            logger.info(f"Saved: {filename}")
    
    def extract_and_organize(self):
        """Main extraction and organization process"""
        logger.info(f"Starting extraction from {self.base_url}/wiki/spaces/{self.space_key}")
        
        # Try API first, then fallback to scraping
        pages = self.get_space_content()
        
        if not pages:
            logger.info("API extraction failed, trying web scraping...")
            pages = self.scrape_public_content()
        
        if pages:
            logger.info(f"Extracted {len(pages)} pages")
            
            # Organize content by category
            organized = self.organize_content(pages)
            
            # Save organized content
            for category, category_pages in organized.items():
                if category_pages:
                    logger.info(f"Saving {len(category_pages)} pages in category: {category}")
                    self.save_content(category_pages, category)
            
            return organized
        else:
            logger.warning("No content extracted")
            return {}


class ContentAnalyzer:
    """Analyze extracted content and suggest documentation improvements"""
    
    def __init__(self, extracted_dir: Path = Path("extracted_content")):
        self.extracted_dir = extracted_dir
        self.suggestions = []
        
    def analyze_content(self) -> Dict:
        """Analyze all extracted content"""
        analysis = {
            'topics_found': {},
            'new_sections_suggested': [],
            'enrichment_opportunities': [],
            'missing_in_docs': []
        }
        
        # Scan all categories
        for category_dir in self.extracted_dir.iterdir():
            if category_dir.is_dir():
                category = category_dir.name
                markdown_files = list(category_dir.glob("*.md"))
                
                if markdown_files:
                    analysis['topics_found'][category] = len(markdown_files)
                    
                    # Analyze content in each file
                    for md_file in markdown_files:
                        self.analyze_file(md_file, category, analysis)
        
        return analysis
    
    def analyze_file(self, file_path: Path, category: str, analysis: Dict):
        """Analyze individual markdown file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Look for specific patterns
            if 'step by step' in content.lower() or 'tutorial' in content.lower():
                analysis['enrichment_opportunities'].append({
                    'file': file_path.name,
                    'category': category,
                    'type': 'tutorial',
                    'suggestion': 'Add to tutorials section'
                })
            
            if 'api' in content.lower() or 'endpoint' in content.lower():
                analysis['enrichment_opportunities'].append({
                    'file': file_path.name,
                    'category': category,
                    'type': 'api',
                    'suggestion': 'Add to API documentation'
                })
            
            if 'troubleshoot' in content.lower() or 'error' in content.lower():
                analysis['enrichment_opportunities'].append({
                    'file': file_path.name,
                    'category': category,
                    'type': 'troubleshooting',
                    'suggestion': 'Add to troubleshooting guide'
                })
            
            # Check for new topics not in current docs
            topics = ['sst', 'gst', 'customs', 'bank integration', 'payroll', 'asset management']
            for topic in topics:
                if topic in content.lower():
                    analysis['missing_in_docs'].append({
                        'topic': topic,
                        'found_in': file_path.name,
                        'category': category
                    })
                    
        except Exception as e:
            logger.error(f"Error analyzing {file_path}: {e}")
    
    def generate_report(self) -> str:
        """Generate analysis report"""
        analysis = self.analyze_content()
        
        report = """# Confluence Content Analysis Report

## Summary
- Total categories found: {}
- Total documents extracted: {}

## Topics Distribution
{}

## Enrichment Opportunities
{}

## Missing Topics in Current Documentation
{}

## Recommended Actions
{}
""".format(
            len(analysis['topics_found']),
            sum(analysis['topics_found'].values()),
            self.format_topics(analysis['topics_found']),
            self.format_opportunities(analysis['enrichment_opportunities']),
            self.format_missing(analysis['missing_in_docs']),
            self.generate_recommendations(analysis)
        )
        
        return report
    
    def format_topics(self, topics: Dict) -> str:
        """Format topics distribution"""
        lines = []
        for category, count in topics.items():
            lines.append(f"- **{category}**: {count} documents")
        return '\n'.join(lines)
    
    def format_opportunities(self, opportunities: List) -> str:
        """Format enrichment opportunities"""
        if not opportunities:
            return "No specific opportunities identified"
        
        lines = []
        for opp in opportunities[:10]:  # Limit to top 10
            lines.append(f"- {opp['file']} ({opp['category']}): {opp['suggestion']}")
        return '\n'.join(lines)
    
    def format_missing(self, missing: List) -> str:
        """Format missing topics"""
        if not missing:
            return "No missing topics identified"
        
        unique_topics = set(item['topic'] for item in missing)
        lines = []
        for topic in unique_topics:
            lines.append(f"- **{topic}**: Consider adding dedicated section")
        return '\n'.join(lines)
    
    def generate_recommendations(self, analysis: Dict) -> str:
        """Generate specific recommendations"""
        recommendations = []
        
        if 'accounting' in analysis['topics_found']:
            recommendations.append("1. Enhance accounting module documentation with Confluence guides")
        
        if 'einvoice' in analysis['topics_found']:
            recommendations.append("2. Update e-invoice section with latest MyInvois procedures")
        
        if 'api' in [opp['type'] for opp in analysis['enrichment_opportunities']]:
            recommendations.append("3. Create comprehensive API reference from extracted content")
        
        if 'setup' in analysis['topics_found']:
            recommendations.append("4. Improve implementation guide with setup procedures")
        
        return '\n'.join(recommendations) if recommendations else "No specific recommendations"


def main():
    """Main execution function"""
    # Configuration
    CONFLUENCE_URL = "https://bigledger.atlassian.net"
    SPACE_KEY = "AKAUN"
    
    # You can set these as environment variables for security
    USERNAME = os.getenv('CONFLUENCE_USERNAME')
    PASSWORD = os.getenv('CONFLUENCE_PASSWORD')
    
    # Extract content
    extractor = ConfluenceExtractor(
        base_url=CONFLUENCE_URL,
        space_key=SPACE_KEY,
        username=USERNAME,
        password=PASSWORD
    )
    
    logger.info("Starting Confluence content extraction...")
    organized_content = extractor.extract_and_organize()
    
    # Analyze extracted content
    logger.info("Analyzing extracted content...")
    analyzer = ContentAnalyzer()
    report = analyzer.generate_report()
    
    # Save report
    report_path = Path("extracted_content/analysis_report.md")
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report)
    
    logger.info(f"Analysis report saved to {report_path}")
    print("\n" + report)
    
    return organized_content


if __name__ == "__main__":
    main()