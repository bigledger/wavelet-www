#!/bin/bash

echo "=== BIGLEDGER NAVIGATION ISSUES REPORT ==="
echo "Generated: $(date)"
echo ""

CONTENT_DIR="content/en"

echo "1. BROKEN INTERNAL PAGE LINKS (excluding images)"
echo "==============================================="

# Extract all internal links from markdown files, excluding image links
grep -r "\](\/" "$CONTENT_DIR" --include="*.md" | \
grep -v "\.svg" | grep -v "\.png" | grep -v "\.jpg" | grep -v "\.jpeg" | grep -v "\.gif" | \
while IFS=: read -r file link_line; do
    # Extract the link path
    link_path=$(echo "$link_line" | sed -n 's/.*\](\([^)]*\)).*/\1/p' | head -1)
    
    if [[ -n "$link_path" ]]; then
        # Remove fragments/anchors
        clean_path=$(echo "$link_path" | sed 's/#.*//')
        
        # Convert to file path
        if [[ "$clean_path" == */ ]]; then
            # Directory link - check for _index.md
            file_path="${CONTENT_DIR}${clean_path}_index.md"
        else
            # File link - add .md if not present
            if [[ "$clean_path" != *.md ]]; then
                file_path="${CONTENT_DIR}${clean_path}.md"
            else
                file_path="${CONTENT_DIR}${clean_path}"
            fi
        fi
        
        # Check if file exists
        if [[ ! -f "$file_path" ]]; then
            echo "BROKEN: $file -> $link_path"
        fi
    fi
done | head -50

echo ""
echo "2. MISSING KEY PAGES REFERENCED IN MAIN INDEX"
echo "=============================================="

# Check specific files referenced in main navigation
key_files=(
    "content/en/user-guide/introduction.md"
    "content/en/developers/postman.md"
    "content/en/developers/applet-sdk.md"
    "content/en/developers/applet-examples.md"
    "content/en/developers/applet-deployment.md"
    "content/en/developers/architecture/data-models.md"
    "content/en/developers/architecture/security.md"
    "content/en/developers/architecture/scalability.md"
    "content/en/developers/scheduling.md"
    "content/en/developers/platform-extensions.md"
    "content/en/developers/multi-tenant.md"
    "content/en/developers/infrastructure.md"
    "content/en/developers/enterprise-auth.md"
)

for file in "${key_files[@]}"; do
    if [[ ! -f "$file" ]]; then
        echo "MISSING: $file"
    fi
done

echo ""
echo "3. STATISTICS"
echo "============="

total_dirs=$(find "$CONTENT_DIR" -type d | wc -l)
dirs_with_index=$(find "$CONTENT_DIR" -name "_index.md" | wc -l)
total_md_files=$(find "$CONTENT_DIR" -name "*.md" | wc -l)

echo "Total directories: $total_dirs"
echo "Directories with _index.md: $dirs_with_index"
echo "Total markdown files: $total_md_files"

if [[ $total_dirs -eq $dirs_with_index ]]; then
    echo "✅ ALL directories have _index.md files"
else
    echo "❌ Missing _index.md files in $((total_dirs - dirs_with_index)) directories"
fi

echo ""
echo "=== END OF REPORT ==="
