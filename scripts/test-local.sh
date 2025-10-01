#!/bin/bash

# Wavelet Website Local Testing Script
# This script builds and tests the site locally before deployment

set -e

echo "🧪 Starting local test environment..."

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Clean and build
echo "Building site..."
rm -rf public/
hugo --gc --minify

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓${NC} Build successful"
    echo ""
    echo "Site statistics:"
    echo "----------------"
    find public -name "*.html" | wc -l | xargs echo "HTML pages:"
    du -sh public | cut -f1 | xargs echo "Total size:"
    echo ""
    echo -e "${GREEN}Starting local server...${NC}"
    echo "Site will be available at: http://localhost:1313"
    echo -e "${YELLOW}Press Ctrl+C to stop${NC}"
    echo ""
    hugo server -D
else
    echo "Build failed!"
    exit 1
fi