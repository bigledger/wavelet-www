#!/bin/bash

# Wavelet Website Consistency Check Script
# This script runs the consistency checker and integrates it with the build process

set -e

echo "🔍 Running Wavelet Website consistency checks..."

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Run the consistency checker
python3 tools/consistency-checker.py "$@"
exit_code=$?

# Check the results
if [ $exit_code -eq 0 ]; then
    echo -e "${GREEN}✅ Consistency check passed! Website is ready for deployment.${NC}"
else
    echo -e "${RED}❌ Consistency check failed. Please review and fix the issues above.${NC}"
    echo ""
    echo "💡 Common fixes:"
    echo "  - Fix broken internal links by updating URLs or creating missing pages"
    echo "  - Add missing _index.md files to directories"
    echo "  - Remove duplicate H1 headers from markdown files"
    echo "  - Review TODO markers and complete pending work"
    echo ""
    echo "📄 Detailed report saved to: consistency-report.json"
fi

exit $exit_code