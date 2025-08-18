#!/usr/bin/env python3
"""
Fix YAML frontmatter issues in markdown files
"""

import os
import re
import yaml
from pathlib import Path

def clean_description(description):
    """Clean description text to avoid YAML issues"""
    if not description:
        return ""
    
    # Remove problematic characters and formatting
    cleaned = description.replace('#', '').replace('**', '').replace('Page ID:', '').replace('Last Updated:', '')
    cleaned = re.sub(r'\s+', ' ', cleaned)  # Normalize whitespace
    cleaned = cleaned.strip()
    
    # Take only first sentence or first 100 characters
    if '.' in cleaned:
        cleaned = cleaned.split('.')[0] + '.'
    else:
        cleaned = cleaned[:100]
    
    return cleaned

def fix_frontmatter(content):
    """Fix YAML frontmatter issues"""
    lines = content.split('\n')
    
    # Find frontmatter boundaries
    if lines[0] != '---':
        return content
    
    frontmatter_end = -1
    for i in range(1, len(lines)):
        if lines[i] == '---':
            frontmatter_end = i
            break
    
    if frontmatter_end == -1:
        return content
    
    # Extract frontmatter and body
    frontmatter_lines = lines[1:frontmatter_end]
    body_lines = lines[frontmatter_end + 1:]
    
    # Parse existing frontmatter
    frontmatter_text = '\n'.join(frontmatter_lines)
    
    try:
        frontmatter_data = yaml.safe_load(frontmatter_text)
        if not frontmatter_data:
            frontmatter_data = {}
    except:
        # If YAML parsing fails, create minimal frontmatter
        frontmatter_data = {}
        
        # Try to extract title from content
        for line in body_lines[:10]:
            if line.startswith('# '):
                frontmatter_data['title'] = line[2:].strip()
                break
    
    # Clean and validate frontmatter
    if 'description' in frontmatter_data:
        frontmatter_data['description'] = clean_description(frontmatter_data['description'])
    elif not frontmatter_data.get('description'):
        # Generate description from first paragraph
        first_paragraph = ""
        for line in body_lines:
            if line.strip() and not line.startswith('#'):
                first_paragraph = line.strip()
                break
        frontmatter_data['description'] = clean_description(first_paragraph)
    
    # Ensure required fields
    if not frontmatter_data.get('title'):
        frontmatter_data['title'] = "Untitled"
    
    if not frontmatter_data.get('weight'):
        frontmatter_data['weight'] = 10
    
    if not frontmatter_data.get('tags'):
        frontmatter_data['tags'] = ['user-guide']
    
    # Generate clean YAML
    clean_yaml = yaml.dump(frontmatter_data, default_flow_style=False, allow_unicode=True)
    
    # Reconstruct content
    new_content = "---\n" + clean_yaml + "---\n" + '\n'.join(body_lines)
    return new_content

def process_file(file_path):
    """Process a single markdown file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        fixed_content = fix_frontmatter(content)
        
        if fixed_content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(fixed_content)
            print(f"Fixed frontmatter: {file_path}")
            return True
        
        return False
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    """Main function to fix all markdown files"""
    
    content_dir = Path('/Users/vincent/repo/blg-wiki/content/en')
    files_fixed = 0
    
    # Process all markdown files
    for file_path in content_dir.rglob('*.md'):
        if process_file(file_path):
            files_fixed += 1
    
    print(f"\nCompleted: {files_fixed} files fixed")

if __name__ == "__main__":
    main()