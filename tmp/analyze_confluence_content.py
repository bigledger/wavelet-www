#!/usr/bin/env python3
"""
Analyze and categorize Confluence content for integration
"""

import os
import re
import json
from pathlib import Path
from collections import defaultdict

def read_file_content(file_path):
    """Read file content safely"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return content
    except:
        return ""

def categorize_content(filename, content):
    """Categorize content based on filename and content analysis"""
    
    # Define categories based on patterns
    categories = {
        'applets': [
            'applet', 'stock_take', 'organization', 'team_maintenance', 
            'group_maintenance', 'pricebook', 'membership', 'process_monitoring',
            'internal_delivery', 'internal_stock', 'unified_contact'
        ],
        'modules': [
            'module', 'core_modules', 'manufacturing', 'time_attendance',
            'delivery_and_installation', 'pts_ccy', 'pts_to_'
        ],
        'ecommerce': [
            'ecomsync', 'cp-commerce', 'shopify', 'marketplace', 'b2b'
        ],
        'industry_solutions': [
            'automotive', 'food_and_beverage', 'industry_guide'
        ],
        'user_guides': [
            'creating_an_item', 'editing_an_item', 'item_maintenance', 
            'document_item', 'group_listing', 'member_', 'team',
            'price_', 'pricing_', 'installation_of_'
        ],
        'business_operations': [
            'dashboard', 'order', 'sales_', 'account_receivable', 'accounting'
        ],
        'inventory_management': [
            'stock_', 'inventory_', 'item_categories', 'items',
            'category_groups', 'dimension_details'
        ],
        'system_admin': [
            'settings', 'installation', 'applet_directory', 'applet_store'
        ],
        'troubleshooting': [
            'troubleshooting', 'faqs'
        ]
    }
    
    filename_lower = filename.lower()
    content_lower = content[:1000].lower()  # First 1000 chars for analysis
    
    # Score each category
    scores = defaultdict(int)
    
    for category, keywords in categories.items():
        for keyword in keywords:
            if keyword in filename_lower:
                scores[category] += 10
            if keyword in content_lower:
                scores[category] += 3
    
    # Special cases based on content analysis
    if 'success story' in content_lower:
        scores['industry_solutions'] += 15
    
    if 'introduction' in filename_lower:
        scores['user_guides'] += 5
    
    if 'overview' in filename_lower or 'overview' in content_lower:
        scores['user_guides'] += 3
        
    # Return the category with highest score
    if scores:
        return max(scores.items(), key=lambda x: x[1])[0]
    else:
        return 'miscellaneous'

def analyze_confluence_content():
    """Main analysis function"""
    
    confluence_dir = Path('/Users/vincent/repo/blg-wiki/tmp/confluence_data')
    
    categorized_content = defaultdict(list)
    content_analysis = []
    
    # Process all markdown files
    for file_path in confluence_dir.glob('*.md'):
        if file_path.name in ['extraction_summary.md', 'raw_pages.json', 'spaces.json']:
            continue
            
        content = read_file_content(file_path)
        category = categorize_content(file_path.name, content)
        
        # Extract basic metadata
        title = ""
        page_id = ""
        last_updated = ""
        
        lines = content.split('\n')
        for i, line in enumerate(lines):
            if line.startswith('# ') and not title:
                title = line[2:].strip()
            elif '**Page ID**:' in line:
                page_id = line.split('**Page ID**:')[1].strip()
            elif '**Last Updated**:' in line:
                last_updated = line.split('**Last Updated**:')[1].strip()
        
        file_info = {
            'filename': file_path.name,
            'title': title,
            'page_id': page_id,
            'last_updated': last_updated,
            'category': category,
            'content_length': len(content),
            'content_preview': content[:200].replace('\n', ' ')
        }
        
        categorized_content[category].append(file_info)
        content_analysis.append(file_info)
    
    # Generate analysis report
    report = {
        'total_files': len(content_analysis),
        'categories': dict(categorized_content),
        'category_counts': {k: len(v) for k, v in categorized_content.items()},
        'all_files': content_analysis
    }
    
    return report

def main():
    print("Analyzing Confluence content...")
    analysis = analyze_confluence_content()
    
    # Save analysis to file
    output_file = '/Users/vincent/repo/blg-wiki/tmp/confluence_analysis.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(analysis, f, indent=2, ensure_ascii=False)
    
    print(f"Analysis saved to: {output_file}")
    
    # Print summary
    print(f"\nAnalysis Summary:")
    print(f"Total files: {analysis['total_files']}")
    print(f"\nCategory breakdown:")
    for category, count in analysis['category_counts'].items():
        print(f"  {category}: {count} files")
    
    return analysis

if __name__ == "__main__":
    main()