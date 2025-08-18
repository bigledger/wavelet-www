#!/usr/bin/env python3
"""
Process existing Confluence data to extract and map images
"""

import json
import re
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def extract_image_references(html_content):
    """Extract all image references from Confluence HTML"""
    images = []
    
    # Pattern for Confluence image macros
    # <ac:image><ri:attachment ri:filename="image.png"/></ac:image>
    pattern = r'<ac:(?:image|inline-image)[^>]*>.*?<ri:attachment\s+ri:filename="([^"]+)".*?</ac:(?:image|inline-image)>'
    
    matches = re.findall(pattern, html_content, re.DOTALL | re.IGNORECASE)
    for filename in matches:
        images.append({
            'type': 'attachment',
            'filename': filename
        })
    
    # Also check for standard img tags (rare in Confluence but possible)
    img_pattern = r'<img[^>]+src="([^"]+)"[^>]*(?:alt="([^"]*)")?'
    img_matches = re.findall(img_pattern, html_content)
    for src, alt in img_matches:
        images.append({
            'type': 'img',
            'src': src,
            'alt': alt or ''
        })
    
    return images

def analyze_confluence_data():
    """Analyze existing Confluence data for images"""
    
    # Load raw pages
    with open('confluence_data/raw_pages.json', 'r') as f:
        data = json.load(f)
    
    pages = data.get('results', [])
    logger.info(f"Analyzing {len(pages)} pages for image references")
    
    image_mapping = {}
    all_images = set()
    pages_with_images = []
    
    for page in pages:
        page_title = page.get('title', 'Unknown')
        page_id = page.get('id', '')
        
        if 'body' in page and 'storage' in page['body']:
            content = page['body']['storage'].get('value', '')
            images = extract_image_references(content)
            
            if images:
                pages_with_images.append({
                    'title': page_title,
                    'id': page_id,
                    'images': images,
                    'image_count': len(images)
                })
                
                # Track all unique images
                for img in images:
                    if img['type'] == 'attachment':
                        all_images.add(img['filename'])
                
                image_mapping[page_title] = images
                logger.info(f"Page '{page_title}' has {len(images)} image(s)")
    
    # Generate report
    report = {
        'total_pages': len(pages),
        'pages_with_images': len(pages_with_images),
        'unique_images': len(all_images),
        'all_image_files': sorted(list(all_images)),
        'pages': pages_with_images
    }
    
    # Save report
    with open('image_analysis_report.json', 'w') as f:
        json.dump(report, f, indent=2)
    
    logger.info(f"\nAnalysis Complete:")
    logger.info(f"Total pages: {report['total_pages']}")
    logger.info(f"Pages with images: {report['pages_with_images']}")
    logger.info(f"Unique image files: {report['unique_images']}")
    logger.info(f"\nTop 10 pages by image count:")
    
    sorted_pages = sorted(pages_with_images, key=lambda x: x['image_count'], reverse=True)
    for page in sorted_pages[:10]:
        logger.info(f"  - {page['title']}: {page['image_count']} images")
    
    return report

def create_image_placeholders(report):
    """Create placeholder images for missing attachments"""
    
    placeholders_dir = Path('placeholder_images')
    placeholders_dir.mkdir(exist_ok=True)
    
    logger.info(f"\nCreating placeholders for {len(report['all_image_files'])} unique images")
    
    # Create a simple SVG placeholder for each image
    for image_file in report['all_image_files']:
        # Determine image type from extension
        ext = Path(image_file).suffix.lower()
        if ext in ['.png', '.jpg', '.jpeg', '.gif', '.svg']:
            placeholder_content = f'''<svg width="800" height="400" xmlns="http://www.w3.org/2000/svg">
  <rect width="800" height="400" fill="#f0f0f0" stroke="#ccc" stroke-width="2"/>
  <text x="400" y="180" font-family="Arial, sans-serif" font-size="24" fill="#666" text-anchor="middle">
    Placeholder for:
  </text>
  <text x="400" y="220" font-family="Arial, sans-serif" font-size="20" fill="#333" text-anchor="middle">
    {image_file}
  </text>
  <text x="400" y="260" font-family="Arial, sans-serif" font-size="14" fill="#999" text-anchor="middle">
    (Original image from Confluence)
  </text>
</svg>'''
            
            # Save as SVG (we'll use SVG for all placeholders)
            placeholder_path = placeholders_dir / f"{Path(image_file).stem}_placeholder.svg"
            with open(placeholder_path, 'w') as f:
                f.write(placeholder_content)
            
            logger.info(f"  Created placeholder for: {image_file}")
    
    logger.info(f"Placeholders saved to: {placeholders_dir}")

def map_to_website_structure(report):
    """Map Confluence pages to website structure"""
    
    # Define mapping rules based on page titles
    mapping_rules = {
        'applets': ['Applet', 'applet'],
        'user-guide': ['User Guide', 'Item', 'Member', 'Price', 'Team', 'Group', 'Document'],
        'business-operations': ['Dashboard', 'Order', 'Sales', 'Account Receivable'],
        'ecommerce': ['EcomSync', 'Ecomsync', 'E-commerce', 'Shopify', 'Marketplace', 'CP-Commerce', 'B2B'],
        'industry-solutions': ['Industry', 'Automotive', 'Food and Beverage', 'Workshop'],
        'modules': ['Module', 'Manufacturing', 'Inventory', 'POS']
    }
    
    page_mappings = []
    
    for page in report['pages']:
        title = page['title']
        target_section = 'general'  # default
        
        # Check which section this page belongs to
        for section, keywords in mapping_rules.items():
            if any(keyword in title for keyword in keywords):
                target_section = section
                break
        
        page_mappings.append({
            'confluence_title': title,
            'target_section': target_section,
            'images': page['images']
        })
    
    # Save mappings
    with open('page_to_section_mappings.json', 'w') as f:
        json.dump(page_mappings, f, indent=2)
    
    logger.info("\nPage to section mappings created")
    
    # Summary by section
    section_summary = {}
    for mapping in page_mappings:
        section = mapping['target_section']
        if section not in section_summary:
            section_summary[section] = {'pages': 0, 'images': 0}
        section_summary[section]['pages'] += 1
        section_summary[section]['images'] += len(mapping['images'])
    
    logger.info("Images by section:")
    for section, stats in section_summary.items():
        logger.info(f"  - {section}: {stats['pages']} pages, {stats['images']} images")
    
    return page_mappings

if __name__ == "__main__":
    # Analyze existing data
    report = analyze_confluence_data()
    
    # Create placeholder images
    create_image_placeholders(report)
    
    # Map to website structure
    mappings = map_to_website_structure(report)
    
    logger.info("\nProcessing complete! Check the generated files:")
    logger.info("  - image_analysis_report.json")
    logger.info("  - page_to_section_mappings.json")
    logger.info("  - placeholder_images/ directory")