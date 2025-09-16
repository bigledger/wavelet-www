#!/bin/bash

echo "=== BIGLEDGER WIKI NAVIGATION AUDIT REPORT ==="
echo "Generated: $(date)"
echo ""

CONTENT_DIR="content/en"
BROKEN_LINKS=()

echo "1. CHECKING FOR BROKEN INTERNAL LINKS"
echo "===================================="

# Extract all internal links from markdown files
grep -r "\](\/" "$CONTENT_DIR" --include="*.md" | while IFS=: read -r file link_line; do
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
            echo "BROKEN: $file -> $link_path (Looking for: $file_path)"
        fi
    fi
done

echo ""
echo "2. DIRECTORY STRUCTURE ANALYSIS"
echo "==============================="

total_dirs=$(find "$CONTENT_DIR" -type d | wc -l)
dirs_with_index=$(find "$CONTENT_DIR" -name "_index.md" | wc -l)
total_md_files=$(find "$CONTENT_DIR" -name "*.md" | wc -l)
non_index_files=$(find "$CONTENT_DIR" -name "*.md" -not -name "_index.md" | wc -l)

echo "Total directories: $total_dirs"
echo "Directories with _index.md: $dirs_with_index"
echo "Total markdown files: $total_md_files"
echo "Non-index content files: $non_index_files"

if [[ $total_dirs -eq $dirs_with_index ]]; then
    echo "✅ ALL directories have _index.md files"
else
    echo "❌ Missing _index.md files in $((total_dirs - dirs_with_index)) directories"
fi

echo ""
echo "3. CRITICAL NAVIGATION FILES STATUS"
echo "===================================="

critical_files=(
    "content/en/_index.md"
    "content/en/user-guide/_index.md"
    "content/en/applets/_index.md"
    "content/en/modules/_index.md"
    "content/en/developers/_index.md"
    "content/en/guides/_index.md"
)

for file in "${critical_files[@]}"; do
    if [[ -f "$file" ]]; then
        echo "✅ $file"
    else
        echo "❌ $file (MISSING)"
    fi
done

echo ""
echo "4. DIRECTORY LISTING BY SECTION"
echo "==============================="

echo ""
echo "APPLETS SECTION:"
find "$CONTENT_DIR/applets" -name "*.md" | wc -l | xargs echo "Total applet files:"

echo ""
echo "USER GUIDE SECTIONS:"
for dir in $(find "$CONTENT_DIR/user-guide" -type d | sort); do
    count=$(find "$dir" -maxdepth 1 -name "*.md" -not -name "_index.md" | wc -l)
    echo "  $(basename "$dir"): $count files"
done

echo ""
echo "MODULE SECTIONS:"
for dir in $(find "$CONTENT_DIR/modules" -type d | sort); do
    count=$(find "$dir" -maxdepth 1 -name "*.md" -not -name "_index.md" | wc -l)
    echo "  $(basename "$dir"): $count files"
done

echo ""
echo "DEVELOPER SECTIONS:"
for dir in $(find "$CONTENT_DIR/developers" -type d | sort); do
    count=$(find "$dir" -maxdepth 1 -name "*.md" -not -name "_index.md" | wc -l)
    echo "  $(basename "$dir"): $count files"
done

echo ""
echo "=== END OF REPORT ==="
