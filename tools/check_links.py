#!/usr/bin/env python3
"""
Comprehensive link checker for Hugo site
Checks all internal links in markdown files and verifies they exist
"""

import os
import re
from pathlib import Path
import sys

def find_all_links(content_dir):
    """Find all internal links in markdown files"""
    links = set()
    link_pattern = re.compile(r'\[([^\]]+)\]\((/[^)]+)\)')
    
    for root, dirs, files in os.walk(content_dir):
        for file in files:
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                        matches = link_pattern.findall(content)
                        for text, link in matches:
                            # Remove anchors and query params
                            clean_link = link.split('#')[0].split('?')[0]
                            if clean_link and not clean_link.startswith('http'):
                                links.add((clean_link, filepath))
                except Exception as e:
                    print(f"Error reading {filepath}: {e}")
    
    return links

def check_link_exists(link, content_dir):
    """Check if a link corresponds to an existing content file"""
    # Remove trailing slash
    link = link.rstrip('/')
    
    # Check for exact file match
    possible_paths = [
        f"content/en{link}.md",
        f"content/en{link}/_index.md",
        f"content/en{link}/index.md",
    ]
    
    for path in possible_paths:
        full_path = os.path.join(os.path.dirname(content_dir), path)
        if os.path.exists(full_path):
            return True
    
    # Check if it's a valid Hugo section
    if link in ['/search', '/', '']:
        return True
        
    return False

def main():
    content_dir = "content/en"
    
    if not os.path.exists(content_dir):
        print(f"Error: {content_dir} directory not found")
        sys.exit(1)
    
    print("Scanning for internal links...")
    all_links = find_all_links(content_dir)
    
    print(f"Found {len(all_links)} internal links")
    print("\nChecking for broken links...\n")
    
    broken_links = []
    checked_links = set()
    
    for link, source_file in sorted(all_links):
        if link not in checked_links:
            checked_links.add(link)
            if not check_link_exists(link, content_dir):
                broken_links.append((link, source_file))
    
    if broken_links:
        print(f"Found {len(broken_links)} broken links:\n")
        for link, source in broken_links:
            source_short = source.replace('content/en/', '')
            print(f"  ❌ {link}")
            print(f"     Found in: {source_short}")
            print()
    else:
        print("✅ No broken links found!")
    
    return len(broken_links)

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)