#!/usr/bin/env python3
"""
Simple Confluence scraper for BigLedger public wiki
"""

import os
import re
import json
import time
import requests
from pathlib import Path
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import html2text

def scrape_confluence_public():
    """Scrape publicly accessible Confluence content"""
    
    base_url = "https://bigledger.atlassian.net"
    wiki_url = f"{base_url}/wiki/spaces/AKAUN/overview"
    
    # Create output directory
    output_dir = Path("tmp/extracted_content")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Initialize html2text converter
    h2t = html2text.HTML2Text()
    h2t.ignore_links = False
    h2t.body_width = 0
    
    print(f"Attempting to access: {wiki_url}")
    
    try:
        # Try to fetch the main page
        response = requests.get(wiki_url, timeout=10)
        print(f"Response status: {response.status_code}")
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Save the main page
            main_content = soup.prettify()
            with open(output_dir / "main_page.html", 'w', encoding='utf-8') as f:
                f.write(main_content)
            
            # Convert to markdown
            markdown = h2t.handle(main_content)
            with open(output_dir / "main_page.md", 'w', encoding='utf-8') as f:
                f.write(markdown)
            
            print(f"Saved main page to {output_dir}")
            
            # Try to find links to other pages
            links = soup.find_all('a', href=True)
            page_links = []
            
            for link in links:
                href = link['href']
                if '/wiki/spaces/AKAUN' in href and 'pages' in href:
                    full_url = urljoin(base_url, href)
                    if full_url not in page_links:
                        page_links.append(full_url)
            
            print(f"Found {len(page_links)} potential page links")
            
            # Save links for reference
            with open(output_dir / "found_links.json", 'w') as f:
                json.dump(page_links, f, indent=2)
                
            return True
            
        else:
            print(f"Could not access the wiki. Status code: {response.status_code}")
            # Save response for debugging
            with open(output_dir / "response_debug.html", 'w', encoding='utf-8') as f:
                f.write(response.text)
            return False
            
    except Exception as e:
        print(f"Error accessing Confluence: {e}")
        return False


def analyze_local_content():
    """Analyze any content we have and suggest documentation improvements"""
    
    suggestions = {
        'potential_sections': [],
        'keywords_found': [],
        'recommended_content': []
    }
    
    # Based on what we know about BigLedger, suggest content areas
    known_topics = {
        'accounting': ['Chart of Accounts', 'Journal Entries', 'Financial Reports', 'GL Setup'],
        'einvoice': ['MyInvois Setup', 'PEPPOL Configuration', 'E-Invoice Validation', 'LHDN Integration'],
        'inventory': ['Stock Management', 'Stock Transfer', 'Stock Adjustment', 'Reorder Points'],
        'sales': ['POS Configuration', 'Sales Orders', 'Customer Management', 'Quotations'],
        'purchasing': ['Purchase Orders', 'Vendor Management', 'GRN Process', 'Purchase Returns'],
        'setup': ['Initial Configuration', 'Company Setup', 'User Permissions', 'Tax Configuration'],
        'integration': ['API Documentation', 'Webhook Setup', 'Third-party Integration', 'Data Import/Export'],
        'reports': ['Financial Reports', 'Sales Analytics', 'Inventory Reports', 'Custom Reports']
    }
    
    # Generate suggestions based on known BigLedger features
    for category, topics in known_topics.items():
        for topic in topics:
            suggestions['potential_sections'].append({
                'category': category,
                'topic': topic,
                'suggested_path': f'/guides/{category}/{topic.lower().replace(" ", "-")}'
            })
    
    # Save suggestions
    output_dir = Path("tmp/extracted_content")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    with open(output_dir / "content_suggestions.json", 'w') as f:
        json.dump(suggestions, f, indent=2)
    
    print(f"Saved content suggestions to {output_dir / 'content_suggestions.json'}")
    
    return suggestions


if __name__ == "__main__":
    print("Starting Confluence content extraction...")
    
    # Try to scrape public content
    success = scrape_confluence_public()
    
    if success:
        print("Successfully scraped some content")
    else:
        print("Could not scrape Confluence directly (may require authentication)")
    
    # Analyze and generate suggestions
    print("\nGenerating content suggestions based on BigLedger features...")
    suggestions = analyze_local_content()
    
    print(f"\nGenerated {len(suggestions['potential_sections'])} content suggestions")
    print("\nTop 10 suggested sections:")
    for item in suggestions['potential_sections'][:10]:
        print(f"  - {item['category']}: {item['topic']}")