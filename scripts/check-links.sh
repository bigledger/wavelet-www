#!/bin/bash

# Wavelet Website Link Checker Script
# This script validates all links in the built site

set -e

echo "🔍 Checking links in the Wavelet Website..."

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Build the site first
echo "Building site..."
hugo --gc --minify > /dev/null 2>&1

echo "Checking internal links..."

# Function to check if file exists
check_link() {
    local file=$1
    local link=$2
    local target=""
    
    # Remove fragment identifier
    link="${link%%#*}"
    
    # Skip external links
    if [[ "$link" =~ ^https?:// ]] || [[ "$link" =~ ^mailto: ]]; then
        return 0
    fi
    
    # Handle absolute paths
    if [[ "$link" =~ ^/ ]]; then
        target="public${link}"
    else
        # Relative path
        dir=$(dirname "$file")
        target="$dir/$link"
    fi
    
    # Add index.html if it's a directory
    if [[ -d "$target" ]]; then
        target="$target/index.html"
    elif [[ ! "$target" =~ \. ]]; then
        # No extension, probably a directory
        target="$target/index.html"
    fi
    
    if [[ -f "$target" ]]; then
        return 0
    else
        echo -e "${RED}✗${NC} Broken link in $(basename $file): $link"
        return 1
    fi
}

# Find all HTML files and check their links
broken_count=0
total_count=0

while IFS= read -r file; do
    # Extract all href and src attributes
    links=$(grep -oE '(href|src)="[^"]*"' "$file" 2>/dev/null | sed 's/.*="\([^"]*\)".*/\1/' || true)
    
    while IFS= read -r link; do
        if [[ -n "$link" ]]; then
            total_count=$((total_count + 1))
            if ! check_link "$file" "$link"; then
                broken_count=$((broken_count + 1))
            fi
        fi
    done <<< "$links"
done < <(find public -name "*.html")

echo ""
echo "Link check complete!"
echo "Total links checked: $total_count"

if [ $broken_count -eq 0 ]; then
    echo -e "${GREEN}✓ No broken links found!${NC}"
else
    echo -e "${RED}✗ Found $broken_count broken links${NC}"
    exit 1
fi