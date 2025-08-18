#!/usr/bin/env python3
"""
Integrate Confluence content into the main documentation structure
"""

import os
import re
import json
import shutil
from pathlib import Path
from datetime import datetime

def read_file_content(file_path):
    """Read file content safely"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return content
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return ""

def write_file_content(file_path, content):
    """Write file content safely"""
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    except Exception as e:
        print(f"Error writing {file_path}: {e}")
        return False

def clean_filename(title):
    """Convert title to clean filename"""
    # Remove special characters and convert to lowercase
    filename = re.sub(r'[^\w\s-]', '', title.lower())
    filename = re.sub(r'[-\s]+', '-', filename)
    return filename.strip('-')

def extract_content_body(content):
    """Extract the main content body from Confluence format"""
    lines = content.split('\n')
    
    # Skip metadata section
    body_start = 0
    in_metadata = False
    
    for i, line in enumerate(lines):
        if line.strip() == '---' and i < 10:
            if not in_metadata:
                in_metadata = True
            else:
                body_start = i + 1
                break
        elif line.startswith('# ') and i < 5:
            body_start = i
            break
    
    # Extract body content
    body_lines = lines[body_start:]
    
    # Remove Confluence-specific formatting
    cleaned_lines = []
    for line in body_lines:
        # Skip empty Confluence metadata
        if line.strip() in ['---', '']:
            continue
        # Convert Confluence-specific formatting
        line = re.sub(r'&rsquo;', "'", line)
        line = re.sub(r'&ldquo;', '"', line)
        line = re.sub(r'&rdquo;', '"', line)
        line = re.sub(r'&mdash;', '—', line)
        line = re.sub(r'&ndash;', '–', line)
        
        cleaned_lines.append(line)
    
    return '\n'.join(cleaned_lines).strip()

def create_hugo_frontmatter(title, description="", weight=10, tags=None):
    """Create Hugo frontmatter"""
    if tags is None:
        tags = []
    
    frontmatter = f"""---
title: "{title}"
description: "{description}"
weight: {weight}
tags: {tags}
---

"""
    return frontmatter

def process_applet_content(source_dir, target_dir, analysis_data):
    """Process applet-related content"""
    applet_files = analysis_data['categories']['applets']
    
    processed_files = []
    
    for file_info in applet_files:
        source_path = os.path.join(source_dir, file_info['filename'])
        content = read_file_content(source_path)
        
        if not content:
            continue
        
        # Extract and clean content
        title = file_info['title'] or file_info['filename'].replace('.md', '').replace('_', ' ')
        body = extract_content_body(content)
        
        if len(body.strip()) < 50:  # Skip very short content
            continue
        
        # Create clean filename
        clean_name = clean_filename(title)
        target_path = os.path.join(target_dir, 'applets', f"{clean_name}.md")
        
        # Create description from first paragraph
        first_paragraph = body.split('\n\n')[0][:150]
        description = re.sub(r'\n', ' ', first_paragraph)
        
        # Create frontmatter and content
        frontmatter = create_hugo_frontmatter(title, description, tags=['applets'])
        full_content = frontmatter + body
        
        # Write file
        if write_file_content(target_path, full_content):
            processed_files.append({
                'source': file_info['filename'],
                'target': target_path,
                'title': title
            })
    
    return processed_files

def process_ecommerce_content(source_dir, target_dir, analysis_data):
    """Process e-commerce related content"""
    ecommerce_files = analysis_data['categories']['ecommerce']
    
    processed_files = []
    
    for file_info in ecommerce_files:
        source_path = os.path.join(source_dir, file_info['filename'])
        content = read_file_content(source_path)
        
        if not content:
            continue
        
        # Extract and clean content
        title = file_info['title'] or file_info['filename'].replace('.md', '').replace('_', ' ')
        body = extract_content_body(content)
        
        if len(body.strip()) < 50:
            continue
        
        # Create clean filename
        clean_name = clean_filename(title)
        target_path = os.path.join(target_dir, 'ecommerce', f"{clean_name}.md")
        
        # Create description
        first_paragraph = body.split('\n\n')[0][:150]
        description = re.sub(r'\n', ' ', first_paragraph)
        
        # Create frontmatter and content
        frontmatter = create_hugo_frontmatter(title, description, tags=['ecommerce', 'integration'])
        full_content = frontmatter + body
        
        # Write file
        if write_file_content(target_path, full_content):
            processed_files.append({
                'source': file_info['filename'],
                'target': target_path,
                'title': title
            })
    
    return processed_files

def process_industry_content(source_dir, target_dir, analysis_data):
    """Process industry-specific content"""
    industry_files = analysis_data['categories']['industry_solutions']
    
    processed_files = []
    
    for file_info in industry_files:
        source_path = os.path.join(source_dir, file_info['filename'])
        content = read_file_content(source_path)
        
        if not content:
            continue
        
        # Extract and clean content
        title = file_info['title'] or file_info['filename'].replace('.md', '').replace('_', ' ')
        body = extract_content_body(content)
        
        if len(body.strip()) < 50:
            continue
        
        # Create clean filename
        clean_name = clean_filename(title)
        target_path = os.path.join(target_dir, 'industry-solutions', f"{clean_name}.md")
        
        # Create description
        first_paragraph = body.split('\n\n')[0][:150]
        description = re.sub(r'\n', ' ', first_paragraph)
        
        # Create frontmatter and content
        frontmatter = create_hugo_frontmatter(title, description, tags=['industry', 'solutions'])
        full_content = frontmatter + body
        
        # Write file
        if write_file_content(target_path, full_content):
            processed_files.append({
                'source': file_info['filename'],
                'target': target_path,
                'title': title
            })
    
    return processed_files

def process_business_operations_content(source_dir, target_dir, analysis_data):
    """Process business operations content"""
    business_files = analysis_data['categories']['business_operations']
    
    processed_files = []
    
    for file_info in business_files:
        source_path = os.path.join(source_dir, file_info['filename'])
        content = read_file_content(source_path)
        
        if not content:
            continue
        
        # Extract and clean content
        title = file_info['title'] or file_info['filename'].replace('.md', '').replace('_', ' ')
        body = extract_content_body(content)
        
        if len(body.strip()) < 50:
            continue
        
        # Create clean filename
        clean_name = clean_filename(title)
        target_path = os.path.join(target_dir, 'business-operations', f"{clean_name}.md")
        
        # Create description
        first_paragraph = body.split('\n\n')[0][:150]
        description = re.sub(r'\n', ' ', first_paragraph)
        
        # Create frontmatter and content
        frontmatter = create_hugo_frontmatter(title, description, tags=['business', 'operations'])
        full_content = frontmatter + body
        
        # Write file
        if write_file_content(target_path, full_content):
            processed_files.append({
                'source': file_info['filename'],
                'target': target_path,
                'title': title
            })
    
    return processed_files

def process_user_guides_content(source_dir, target_dir, analysis_data):
    """Process user guides content"""
    user_guide_files = analysis_data['categories']['user_guides']
    
    processed_files = []
    
    for file_info in user_guide_files:
        source_path = os.path.join(source_dir, file_info['filename'])
        content = read_file_content(source_path)
        
        if not content:
            continue
        
        # Extract and clean content
        title = file_info['title'] or file_info['filename'].replace('.md', '').replace('_', ' ')
        body = extract_content_body(content)
        
        if len(body.strip()) < 50:
            continue
        
        # Create clean filename
        clean_name = clean_filename(title)
        target_path = os.path.join(target_dir, 'user-guide', f"{clean_name}.md")
        
        # Create description
        first_paragraph = body.split('\n\n')[0][:150]
        description = re.sub(r'\n', ' ', first_paragraph)
        
        # Create frontmatter and content
        frontmatter = create_hugo_frontmatter(title, description, tags=['user-guide', 'tutorial'])
        full_content = frontmatter + body
        
        # Write file
        if write_file_content(target_path, full_content):
            processed_files.append({
                'source': file_info['filename'],
                'target': target_path,
                'title': title
            })
    
    return processed_files

def create_index_pages(target_dir):
    """Create index pages for new sections"""
    
    # Business Operations index
    business_index = create_hugo_frontmatter(
        "Business Operations",
        "Day-to-day business operations and workflow management with BigLedger",
        1,
        ['business', 'operations', 'workflow']
    ) + """
# Business Operations

This section covers the day-to-day business operations and workflow management within BigLedger. Learn how to manage your core business processes efficiently and effectively.

## Core Business Processes

BigLedger streamlines your essential business operations through integrated modules and applets that work together seamlessly.

### Key Areas Covered

- **Dashboard Management** - Monitor key business metrics and KPIs
- **Sales Operations** - Handle sales orders, quotations, and customer management
- **Financial Operations** - Manage accounting, receivables, and financial reporting
- **Order Management** - Process orders from creation to fulfillment

## Getting Started

Navigate through the topics below to learn about specific business operations within BigLedger.
"""
    
    # Industry Solutions index
    industry_index = create_hugo_frontmatter(
        "Industry Solutions",
        "Industry-specific implementations and success stories with BigLedger",
        1,
        ['industry', 'solutions', 'case-studies']
    ) + """
# Industry Solutions

BigLedger serves businesses across multiple industries with tailored solutions and specialized workflows. This section showcases industry-specific implementations and success stories.

## Supported Industries

BigLedger has been successfully implemented across various industries, each with unique requirements and challenges.

### Key Industries

- **Automotive and Workshop** - Service centers, parts management, and customer engagement
- **Food and Beverage** - Multi-branch operations, inventory management, and POS integration
- **Manufacturing** - Production planning, quality control, and supply chain optimization
- **Retail** - Point of sale, inventory management, and customer loyalty programs

## Implementation Approach

Each industry implementation is customized to address specific business requirements while leveraging BigLedger's core platform capabilities.
"""
    
    # E-commerce index
    ecommerce_index = create_hugo_frontmatter(
        "E-commerce Integration",
        "Multi-channel e-commerce operations with EcomSync and CP-Commerce",
        1,
        ['ecommerce', 'integration', 'multi-channel']
    ) + """
# E-commerce Integration

BigLedger's e-commerce solutions enable seamless multi-channel operations through EcomSync and CP-Commerce modules. Manage your online presence across multiple platforms while maintaining centralized inventory and order management.

## Core E-commerce Features

- **EcomSync Module** - Centralized multi-channel e-commerce management
- **CP-Commerce** - Comprehensive e-commerce platform
- **Marketplace Integration** - Connect with Shopee, Lazada, and other platforms
- **B2B Solutions** - Business-to-business e-commerce capabilities

## Key Benefits

- Centralized inventory management across all channels
- Real-time synchronization of stock levels and pricing
- Unified order management and fulfillment
- Comprehensive reporting and analytics

## Getting Started

Explore the topics below to set up and optimize your e-commerce operations with BigLedger.
"""
    
    # Applets index
    applets_index = create_hugo_frontmatter(
        "Applets and Workflows",
        "Comprehensive guide to BigLedger applets and workflow automation",
        1,
        ['applets', 'workflows', 'automation']
    ) + """
# Applets and Workflows

BigLedger's modular approach centers around applets - specialized mini-applications that handle specific business functions. This section provides comprehensive documentation for all available applets and their workflows.

## What are Applets?

Applets are lightweight, focused applications that can be installed and configured independently. They integrate seamlessly with BigLedger's core platform and other applets to create comprehensive business solutions.

## Applet Categories

### Core Operations
- **Stock Take Applet** - Digital inventory counting and management
- **Organization Applet** - Company, branch, and location management
- **Team Maintenance** - User and team management

### Business Intelligence
- **Process Monitoring** - Track and analyze business processes
- **Membership Admin Console** - Customer loyalty and membership programs

### Integration & Automation
- **Internal Delivery Order** - Manage internal transfers and deliveries
- **Internal Stock Adjustment** - Handle inventory adjustments and corrections

## Installation and Management

Learn how to install, configure, and manage applets through the Applet Store and directory system.
"""
    
    # Write index pages
    index_pages = [
        ('/Users/vincent/repo/blg-wiki/content/en/business-operations/_index.md', business_index),
        ('/Users/vincent/repo/blg-wiki/content/en/industry-solutions/_index.md', industry_index),
        ('/Users/vincent/repo/blg-wiki/content/en/ecommerce/_index.md', ecommerce_index),
        ('/Users/vincent/repo/blg-wiki/content/en/applets/_index.md', applets_index)
    ]
    
    created_pages = []
    for path, content in index_pages:
        if write_file_content(path, content):
            created_pages.append(path)
    
    return created_pages

def main():
    """Main integration function"""
    
    # Paths
    source_dir = '/Users/vincent/repo/blg-wiki/tmp/confluence_data'
    target_dir = '/Users/vincent/repo/blg-wiki/content/en'
    analysis_file = '/Users/vincent/repo/blg-wiki/tmp/confluence_analysis.json'
    
    # Load analysis data
    with open(analysis_file, 'r') as f:
        analysis_data = json.load(f)
    
    print("Starting Confluence content integration...")
    
    # Process different content types
    integration_results = {
        'applets': process_applet_content(source_dir, target_dir, analysis_data),
        'ecommerce': process_ecommerce_content(source_dir, target_dir, analysis_data),
        'industry_solutions': process_industry_content(source_dir, target_dir, analysis_data),
        'business_operations': process_business_operations_content(source_dir, target_dir, analysis_data),
        'user_guides': process_user_guides_content(source_dir, target_dir, analysis_data)
    }
    
    # Create index pages
    index_pages = create_index_pages(target_dir)
    
    # Generate summary
    total_processed = sum(len(files) for files in integration_results.values())
    
    print(f"\nIntegration completed successfully!")
    print(f"Total files processed: {total_processed}")
    for category, files in integration_results.items():
        print(f"  {category}: {len(files)} files")
    print(f"Index pages created: {len(index_pages)}")
    
    # Save detailed results
    results = {
        'timestamp': datetime.now().isoformat(),
        'total_processed': total_processed,
        'integration_results': integration_results,
        'index_pages_created': index_pages,
        'source_analysis': analysis_data
    }
    
    results_file = '/Users/vincent/repo/blg-wiki/tmp/integration_results.json'
    with open(results_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"Detailed results saved to: {results_file}")
    
    return results

if __name__ == "__main__":
    main()