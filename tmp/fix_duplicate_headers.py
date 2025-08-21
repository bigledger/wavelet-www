#!/usr/bin/env python3
"""
Script to find and fix duplicate headers in markdown files
"""

import os
import re
from pathlib import Path

def find_duplicate_headers(content, filename):
    """Find duplicate headers in markdown content"""
    lines = content.split('\n')
    
    # Get the title from frontmatter
    frontmatter_title = None
    in_frontmatter = False
    for line in lines:
        if line.strip() == '---':
            if in_frontmatter:
                break
            in_frontmatter = True
        elif in_frontmatter and line.startswith('title:'):
            frontmatter_title = line.replace('title:', '').strip().strip('"').strip("'")
    
    # Find all headers
    headers = []
    header_lines = []
    for i, line in enumerate(lines):
        if line.startswith('#'):
            # Extract header text (remove # and strip)
            header_match = re.match(r'^#+\s+(.+)$', line)
            if header_match:
                header_text = header_match.group(1).strip()
                headers.append(header_text)
                header_lines.append((i, line, header_text))
    
    # Check for duplicates
    duplicates = []
    seen = set()
    for i, (line_num, line, header) in enumerate(header_lines):
        # Check if this header matches the frontmatter title
        if frontmatter_title and header == frontmatter_title:
            duplicates.append((line_num, line, header, 'matches_frontmatter'))
        # Check for consecutive duplicate headers
        elif i > 0 and header == header_lines[i-1][2]:
            duplicates.append((line_num, line, header, 'consecutive_duplicate'))
        # Check for any duplicate headers
        elif header in seen:
            duplicates.append((line_num, line, header, 'duplicate'))
        seen.add(header)
    
    return duplicates, frontmatter_title, lines

def fix_duplicate_headers(content, filename):
    """Fix duplicate headers in markdown content"""
    duplicates, frontmatter_title, lines = find_duplicate_headers(content, filename)
    
    if not duplicates:
        return content, False
    
    print(f"\n📄 {filename}")
    print(f"   Found {len(duplicates)} duplicate headers")
    
    # Track lines to remove
    lines_to_remove = set()
    
    for line_num, line, header, dup_type in duplicates:
        if dup_type == 'consecutive_duplicate':
            # Remove the second occurrence of consecutive duplicates
            lines_to_remove.add(line_num)
            print(f"   - Removing duplicate header on line {line_num + 1}: '{header}'")
        elif dup_type == 'matches_frontmatter' and line_num < 20:  # Only if near the top
            # Check if this is the first content header and matches title
            content_start = -1
            for i, l in enumerate(lines):
                if l.strip() == '---':
                    if content_start == -1:
                        content_start = i
                    else:
                        content_start = i + 1
                        break
            
            # If this header is right after frontmatter and matches title, consider removing
            if content_start > 0 and line_num - content_start < 5:
                # Check if there's meaningful content between frontmatter and this header
                has_content = False
                for i in range(content_start, line_num):
                    if lines[i].strip() and not lines[i].startswith('#'):
                        has_content = True
                        break
                
                if not has_content:
                    lines_to_remove.add(line_num)
                    print(f"   - Removing redundant title header on line {line_num + 1}: '{header}'")
    
    # Remove the duplicate lines
    if lines_to_remove:
        new_lines = []
        for i, line in enumerate(lines):
            if i not in lines_to_remove:
                new_lines.append(line)
            else:
                # Check if the next line is blank, if not, keep one blank line
                if i + 1 < len(lines) and lines[i + 1].strip() != '':
                    if i == 0 or lines[i - 1].strip() != '':
                        new_lines.append('')
        
        # Clean up multiple consecutive blank lines
        final_lines = []
        prev_blank = False
        for line in new_lines:
            if line.strip() == '':
                if not prev_blank:
                    final_lines.append(line)
                prev_blank = True
            else:
                final_lines.append(line)
                prev_blank = False
        
        return '\n'.join(final_lines), True
    
    return content, False

def process_directory(directory):
    """Process all markdown files in a directory"""
    content_dir = Path(directory)
    modified_files = []
    
    print("🔍 Scanning for duplicate headers...\n")
    
    for md_file in content_dir.rglob('*.md'):
        # Skip _index.md files as they might have special formatting
        if md_file.name == '_index.md':
            continue
            
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content, was_modified = fix_duplicate_headers(content, md_file.relative_to(content_dir))
        
        if was_modified:
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            modified_files.append(str(md_file.relative_to(content_dir)))
    
    return modified_files

def main():
    # Process the content/en directory
    content_dir = Path('/Users/vincent/repo/blg-wiki/content/en')
    
    if not content_dir.exists():
        print("❌ Content directory not found!")
        return
    
    modified = process_directory(content_dir)
    
    print("\n" + "="*50)
    print("✅ Duplicate header cleanup complete!")
    print(f"📊 Modified {len(modified)} files")
    
    if modified:
        print("\n📝 Files modified:")
        for file in modified:
            print(f"   - {file}")

if __name__ == "__main__":
    main()