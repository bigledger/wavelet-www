#!/usr/bin/env python3
"""
Fix card shortcode syntax across all files
"""

import os
import re
from pathlib import Path

def fix_card_shortcodes(content):
    """Fix card shortcode syntax from closing tag format to subtitle format"""
    
    # Pattern to match card shortcodes with closing tags
    pattern = r'{{< card ([^>]+)>}}\n([^\n]+)\n{{< /card >}}'
    
    def replace_card(match):
        attributes = match.group(1)
        subtitle_text = match.group(2).strip()
        
        # Add subtitle attribute if it doesn't exist
        if 'subtitle=' not in attributes:
            attributes += f' subtitle="{subtitle_text}"'
        
        return f'{{{{< card {attributes} >}}}}'
    
    # Apply the replacement
    fixed_content = re.sub(pattern, replace_card, content, flags=re.MULTILINE)
    return fixed_content

def process_file(file_path):
    """Process a single markdown file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        fixed_content = fix_card_shortcodes(content)
        
        if fixed_content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(fixed_content)
            print(f"Fixed: {file_path}")
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