#!/usr/bin/env python3
"""
Multi-Method Confluence Content Extractor
Tries various approaches to extract content from Confluence
"""

import os
import re
import json
import time
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Dict, List, Optional, Any
from urllib.parse import urljoin, urlparse, quote
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class ConfluenceMultiExtractor:
    """Multiple extraction methods for Confluence content"""
    
    def __init__(self, base_url: str = "https://bigledger.atlassian.net", 
                 space_key: str = "AKAUN"):
        self.base_url = base_url
        self.space_key = space_key
        self.wiki_base = f"{base_url}/wiki"
        self.results = []
        self.output_dir = Path("tmp/confluence_extraction")
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
    def method1_rest_api_anonymous(self) -> List[Dict]:
        """Try REST API endpoints without authentication"""
        logger.info("Method 1: Trying anonymous REST API access...")
        
        endpoints = [
            f"/wiki/rest/api/content?spaceKey={self.space_key}&limit=100",
            f"/wiki/rest/api/space/{self.space_key}",
            f"/wiki/rest/api/space/{self.space_key}/content",
            f"/wiki/rest/api/space/{self.space_key}/content/page",
            f"/wiki/rest/api/search?cql=space={self.space_key}",
            f"/wiki/api/v2/spaces/{self.space_key}/pages",
            f"/wiki/api/v2/pages",
            f"/rest/api/content/search?cql=space={self.space_key}",
        ]
        
        results = []
        try:
            import requests
            session = requests.Session()
            session.headers.update({
                'Accept': 'application/json',
                'User-Agent': 'Mozilla/5.0 (compatible; Documentation Bot)'
            })
            
            for endpoint in endpoints:
                url = self.base_url + endpoint
                logger.info(f"  Trying: {url}")
                try:
                    response = session.get(url, timeout=5)
                    if response.status_code == 200:
                        logger.info(f"    ✓ Success! Got data from {endpoint}")
                        data = response.json()
                        results.append({
                            'endpoint': endpoint,
                            'data': data,
                            'status': 'success'
                        })
                        # Save the response
                        filename = self.output_dir / f"api_{endpoint.replace('/', '_')}.json"
                        with open(filename, 'w') as f:
                            json.dump(data, f, indent=2)
                    else:
                        logger.info(f"    ✗ Status {response.status_code}")
                except Exception as e:
                    logger.debug(f"    ✗ Error: {str(e)}")
                    
        except ImportError:
            logger.error("requests library not available")
            
        return results
    
    def method2_rss_feeds(self) -> List[Dict]:
        """Try to access RSS/Atom feeds"""
        logger.info("Method 2: Checking for RSS/Atom feeds...")
        
        feed_urls = [
            f"/wiki/spaces/{self.space_key}/syndication",
            f"/wiki/spaces/{self.space_key}/rss",
            f"/wiki/spaces/{self.space_key}/atom",
            f"/wiki/spaces/{self.space_key}/activity",
            f"/wiki/spaces/createrssfeed.action?spaces={self.space_key}",
            f"/wiki/createrssfeed.action?types=page&spaces={self.space_key}",
            f"/wiki/spaces/{self.space_key}/blog/feed",
        ]
        
        results = []
        try:
            import requests
            session = requests.Session()
            
            for feed_path in feed_urls:
                url = self.base_url + feed_path
                logger.info(f"  Trying feed: {url}")
                try:
                    response = session.get(url, timeout=5)
                    if response.status_code == 200 and (
                        'xml' in response.headers.get('content-type', '') or
                        'rss' in response.headers.get('content-type', '') or
                        'atom' in response.headers.get('content-type', '')
                    ):
                        logger.info(f"    ✓ Found feed!")
                        results.append({
                            'url': url,
                            'content': response.text,
                            'type': 'feed'
                        })
                        # Save feed
                        filename = self.output_dir / f"feed_{feed_path.replace('/', '_')}.xml"
                        with open(filename, 'w') as f:
                            f.write(response.text)
                except Exception as e:
                    logger.debug(f"    ✗ Error: {str(e)}")
                    
        except ImportError:
            logger.error("requests library not available")
            
        return results
    
    def method3_sitemap(self) -> List[Dict]:
        """Check for sitemap.xml"""
        logger.info("Method 3: Looking for sitemap...")
        
        sitemap_urls = [
            "/sitemap.xml",
            "/wiki/sitemap.xml",
            f"/wiki/spaces/{self.space_key}/sitemap.xml",
            "/robots.txt",
        ]
        
        results = []
        try:
            import requests
            session = requests.Session()
            
            for sitemap_path in sitemap_urls:
                url = self.base_url + sitemap_path
                logger.info(f"  Checking: {url}")
                try:
                    response = session.get(url, timeout=5)
                    if response.status_code == 200:
                        logger.info(f"    ✓ Found {sitemap_path}")
                        results.append({
                            'url': url,
                            'content': response.text,
                            'type': 'sitemap'
                        })
                        # Save
                        filename = self.output_dir / f"sitemap_{sitemap_path.replace('/', '_')}"
                        with open(filename, 'w') as f:
                            f.write(response.text)
                            
                        # Parse sitemap for URLs
                        if 'xml' in sitemap_path:
                            urls = self.parse_sitemap(response.text)
                            logger.info(f"    Found {len(urls)} URLs in sitemap")
                            
                except Exception as e:
                    logger.debug(f"    ✗ Error: {str(e)}")
                    
        except ImportError:
            logger.error("requests library not available")
            
        return results
    
    def method4_public_pages(self) -> List[Dict]:
        """Try to access potentially public pages"""
        logger.info("Method 4: Checking for public pages...")
        
        # Common Confluence page patterns
        page_patterns = [
            f"/wiki/spaces/{self.space_key}/overview",
            f"/wiki/spaces/{self.space_key}/pages",
            f"/wiki/display/{self.space_key}",
            f"/wiki/display/{self.space_key}/Home",
            f"/wiki/display/{self.space_key}/Overview",
            f"/wiki/display/{self.space_key}/Documentation",
            f"/wiki/spaces/{self.space_key}/pages/viewpage.action",
            f"/wiki/spaces/{self.space_key}/pages/viewrecentblogposts.action",
            f"/wiki/spaces/{self.space_key}/pages/listpages.action",
        ]
        
        results = []
        try:
            import requests
            from bs4 import BeautifulSoup
            
            session = requests.Session()
            session.headers.update({
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            })
            
            for pattern in page_patterns:
                url = self.base_url + pattern
                logger.info(f"  Trying: {url}")
                try:
                    response = session.get(url, timeout=5, allow_redirects=True)
                    if response.status_code == 200:
                        logger.info(f"    ✓ Accessible: {pattern}")
                        
                        # Parse for links
                        soup = BeautifulSoup(response.text, 'html.parser')
                        page_links = []
                        
                        # Find all Confluence page links
                        for link in soup.find_all('a', href=True):
                            href = link['href']
                            if f'/spaces/{self.space_key}' in href or f'/display/{self.space_key}' in href:
                                full_url = urljoin(self.base_url, href)
                                if full_url not in page_links:
                                    page_links.append(full_url)
                        
                        logger.info(f"    Found {len(page_links)} page links")
                        
                        results.append({
                            'url': url,
                            'status': response.status_code,
                            'links_found': page_links,
                            'content_length': len(response.text)
                        })
                        
                        # Save page
                        filename = self.output_dir / f"page_{pattern.replace('/', '_')}.html"
                        with open(filename, 'w') as f:
                            f.write(response.text)
                            
                except Exception as e:
                    logger.debug(f"    ✗ Error: {str(e)}")
                    
        except ImportError:
            logger.error("BeautifulSoup not available")
            
        return results
    
    def method5_search_api(self) -> List[Dict]:
        """Try search API endpoints"""
        logger.info("Method 5: Testing search API...")
        
        search_endpoints = [
            f"/wiki/rest/api/search?cql=space={self.space_key}",
            f"/wiki/rest/api/content/search?cql=space={self.space_key}",
            f"/wiki/rest/searchv3/1.0/search?where={self.space_key}",
            f"/wiki/rest/prototype/1/search/site?query={self.space_key}",
            f"/wiki/api/v2/search?q=space:{self.space_key}",
        ]
        
        results = []
        try:
            import requests
            session = requests.Session()
            
            for endpoint in search_endpoints:
                url = self.base_url + endpoint
                logger.info(f"  Trying search: {url}")
                try:
                    response = session.get(url, timeout=5)
                    if response.status_code == 200:
                        logger.info(f"    ✓ Search accessible!")
                        data = response.json() if 'json' in response.headers.get('content-type', '') else response.text
                        results.append({
                            'endpoint': endpoint,
                            'data': data
                        })
                except Exception as e:
                    logger.debug(f"    ✗ Error: {str(e)}")
                    
        except ImportError:
            logger.error("requests library not available")
            
        return results
    
    def method6_export_endpoints(self) -> List[Dict]:
        """Try export endpoints"""
        logger.info("Method 6: Checking export endpoints...")
        
        export_urls = [
            f"/wiki/spaces/exportspace.action?key={self.space_key}",
            f"/wiki/spaces/{self.space_key}/exportspace.action",
            f"/wiki/exportword?pageId=",
            f"/wiki/spaces/flyingpdf/pdfpageexport.action?pageId=",
            f"/wiki/spaces/{self.space_key}/export",
        ]
        
        results = []
        try:
            import requests
            session = requests.Session()
            
            for export_url in export_urls:
                url = self.base_url + export_url
                logger.info(f"  Checking export: {url}")
                try:
                    # Just check if accessible, don't download
                    response = session.head(url, timeout=5, allow_redirects=True)
                    if response.status_code in [200, 405]:  # 405 means endpoint exists but wrong method
                        logger.info(f"    ✓ Export endpoint exists")
                        results.append({
                            'url': url,
                            'status': response.status_code,
                            'type': 'export'
                        })
                except Exception as e:
                    logger.debug(f"    ✗ Error: {str(e)}")
                    
        except ImportError:
            logger.error("requests library not available")
            
        return results
    
    def method7_graphql(self) -> List[Dict]:
        """Try GraphQL endpoints"""
        logger.info("Method 7: Testing GraphQL...")
        
        graphql_endpoints = [
            "/wiki/graphql",
            "/graphql",
            "/api/graphql",
            "/gateway/api/graphql",
        ]
        
        # Basic GraphQL query to get spaces
        query = {
            "query": """
            {
                spaces {
                    id
                    key
                    name
                    type
                }
            }
            """
        }
        
        results = []
        try:
            import requests
            session = requests.Session()
            session.headers.update({
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            })
            
            for endpoint in graphql_endpoints:
                url = self.base_url + endpoint
                logger.info(f"  Trying GraphQL: {url}")
                try:
                    response = session.post(url, json=query, timeout=5)
                    if response.status_code == 200:
                        logger.info(f"    ✓ GraphQL endpoint accessible!")
                        results.append({
                            'endpoint': endpoint,
                            'data': response.json()
                        })
                except Exception as e:
                    logger.debug(f"    ✗ Error: {str(e)}")
                    
        except ImportError:
            logger.error("requests library not available")
            
        return results
    
    def method8_mobile_api(self) -> List[Dict]:
        """Try mobile API endpoints"""
        logger.info("Method 8: Testing mobile API...")
        
        mobile_endpoints = [
            f"/wiki/rest/mobile/1.0/space/{self.space_key}",
            f"/wiki/rest/mobile/latest/space/{self.space_key}",
            f"/wiki/plugins/servlet/mobile/",
            f"/wiki/rest/mobile/1.0/content/search?spaceKey={self.space_key}",
        ]
        
        results = []
        try:
            import requests
            session = requests.Session()
            session.headers.update({
                'User-Agent': 'Confluence Mobile/1.0'
            })
            
            for endpoint in mobile_endpoints:
                url = self.base_url + endpoint
                logger.info(f"  Trying mobile: {url}")
                try:
                    response = session.get(url, timeout=5)
                    if response.status_code == 200:
                        logger.info(f"    ✓ Mobile API accessible!")
                        results.append({
                            'endpoint': endpoint,
                            'data': response.text[:500]  # First 500 chars
                        })
                except Exception as e:
                    logger.debug(f"    ✗ Error: {str(e)}")
                    
        except ImportError:
            logger.error("requests library not available")
            
        return results
    
    def method9_activity_stream(self) -> List[Dict]:
        """Try activity stream endpoints"""
        logger.info("Method 9: Checking activity streams...")
        
        activity_urls = [
            f"/wiki/activity?key={self.space_key}",
            f"/wiki/spaces/{self.space_key}/activity",
            f"/wiki/rest/activity-stream/1.0/feed?spaceKey={self.space_key}",
            f"/wiki/plugins/recently-updated/changes.action?spaceKey={self.space_key}",
        ]
        
        results = []
        try:
            import requests
            session = requests.Session()
            
            for activity_url in activity_urls:
                url = self.base_url + activity_url
                logger.info(f"  Trying activity: {url}")
                try:
                    response = session.get(url, timeout=5)
                    if response.status_code == 200:
                        logger.info(f"    ✓ Activity stream accessible!")
                        results.append({
                            'url': url,
                            'content_length': len(response.text)
                        })
                except Exception as e:
                    logger.debug(f"    ✗ Error: {str(e)}")
                    
        except ImportError:
            logger.error("requests library not available")
            
        return results
    
    def method10_cached_versions(self) -> Dict:
        """Check for cached versions"""
        logger.info("Method 10: Checking cached/archived versions...")
        
        urls_to_check = [
            f"{self.base_url}/wiki/spaces/{self.space_key}/overview",
            f"{self.base_url}/wiki/display/{self.space_key}",
        ]
        
        results = {
            'wayback': [],
            'google_cache': []
        }
        
        for url in urls_to_check:
            # Wayback Machine
            wayback_url = f"https://web.archive.org/web/*/{url}"
            logger.info(f"  Wayback Machine: {wayback_url}")
            results['wayback'].append(wayback_url)
            
            # Google Cache
            google_cache = f"https://webcache.googleusercontent.com/search?q=cache:{quote(url)}"
            logger.info(f"  Google Cache: {google_cache}")
            results['google_cache'].append(google_cache)
        
        return results
    
    def parse_sitemap(self, xml_content: str) -> List[str]:
        """Parse sitemap XML for URLs"""
        urls = []
        try:
            root = ET.fromstring(xml_content)
            # Handle different sitemap namespaces
            namespaces = {
                '': 'http://www.sitemaps.org/schemas/sitemap/0.9',
                'sitemap': 'http://www.sitemaps.org/schemas/sitemap/0.9'
            }
            
            # Try both with and without namespace
            for url_elem in root.findall('.//url/loc', namespaces):
                urls.append(url_elem.text)
            for url_elem in root.findall('.//loc'):
                urls.append(url_elem.text)
                
        except Exception as e:
            logger.error(f"Error parsing sitemap: {e}")
            
        return urls
    
    def run_all_methods(self) -> Dict:
        """Run all extraction methods"""
        logger.info("=" * 60)
        logger.info("Starting multi-method Confluence extraction")
        logger.info(f"Target: {self.base_url}/wiki/spaces/{self.space_key}")
        logger.info("=" * 60)
        
        all_results = {
            'rest_api': self.method1_rest_api_anonymous(),
            'rss_feeds': self.method2_rss_feeds(),
            'sitemap': self.method3_sitemap(),
            'public_pages': self.method4_public_pages(),
            'search_api': self.method5_search_api(),
            'export_endpoints': self.method6_export_endpoints(),
            'graphql': self.method7_graphql(),
            'mobile_api': self.method8_mobile_api(),
            'activity_stream': self.method9_activity_stream(),
            'cached_versions': self.method10_cached_versions(),
        }
        
        # Save summary
        summary_file = self.output_dir / "extraction_summary.json"
        with open(summary_file, 'w') as f:
            json.dump(all_results, f, indent=2, default=str)
        
        logger.info("\n" + "=" * 60)
        logger.info("EXTRACTION SUMMARY")
        logger.info("=" * 60)
        
        successful_methods = []
        for method, results in all_results.items():
            if results and len(results) > 0:
                successful_methods.append(method)
                logger.info(f"✓ {method}: Found {len(results)} results")
            else:
                logger.info(f"✗ {method}: No results")
        
        logger.info(f"\nSuccessful methods: {', '.join(successful_methods) if successful_methods else 'None'}")
        logger.info(f"Results saved to: {self.output_dir}")
        
        return all_results
    
    def generate_recommendations(self, results: Dict) -> str:
        """Generate recommendations based on results"""
        recommendations = []
        
        if results['rest_api']:
            recommendations.append("REST API is partially accessible - explore more endpoints")
        
        if results['rss_feeds']:
            recommendations.append("RSS feeds found - can monitor for updates")
        
        if results['public_pages']:
            recommendations.append("Some pages are public - can scrape with BeautifulSoup")
        
        if results['cached_versions']:
            recommendations.append("Check Wayback Machine and Google Cache for historical content")
        
        if not any(results.values()):
            recommendations.append("Content is fully restricted - need authentication")
            recommendations.append("Consider requesting API access from BigLedger")
            recommendations.append("Alternative: Request documentation export from team")
        
        return "\n".join(recommendations)


def main():
    """Main execution"""
    extractor = ConfluenceMultiExtractor()
    results = extractor.run_all_methods()
    
    # Generate recommendations
    recommendations = extractor.generate_recommendations(results)
    
    print("\n" + "=" * 60)
    print("RECOMMENDATIONS")
    print("=" * 60)
    print(recommendations)
    
    return results


if __name__ == "__main__":
    main()