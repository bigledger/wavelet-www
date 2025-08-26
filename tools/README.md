# BigLedger Wiki Tools

This directory contains tools for maintaining the BigLedger wiki quality and consistency.

## Consistency Checker

The consistency checker ensures the wiki maintains quality standards across all documentation.

### Features

1. **Navigation Consistency**: Verifies menu is same across all pages
2. **No Duplicate Headers**: Checks for duplicate H1 headers in markdown files
3. **No Broken Internal Links**: Verifies all internal links point to existing pages
4. **Proper File Structure**: Ensures all content follows the agreed structure
5. **Front Matter Validation**: Checks that front matter doesn't override navigation
6. **TODO Tracking**: Lists all TODO markers for tracking incomplete content

### Usage

#### Basic Usage
```bash
# Run consistency check
python3 tools/consistency-checker.py

# Run with verbose output
python3 tools/consistency-checker.py --verbose

# Run via convenience script
./scripts/consistency-check.sh
```

#### Options
```bash
# Only generate report, don't suggest fixes
python3 tools/consistency-checker.py --report-only

# Specify custom output file
python3 tools/consistency-checker.py --output my-report.json

# Check different content directory
python3 tools/consistency-checker.py --content-dir content/zh

# Use different Hugo config
python3 tools/consistency-checker.py --config custom-hugo.yaml
```

### Output

The tool provides:
- **Console report**: Summary of issues found
- **JSON report**: Detailed machine-readable report saved to `consistency-report.json`
- **Exit codes**: 
  - `0`: No critical errors found
  - `1`: Critical errors found that should block deployment

### Integration

#### Pre-commit Integration
Add to your pre-commit workflow:
```bash
#!/bin/bash
./scripts/consistency-check.sh
if [ $? -ne 0 ]; then
    echo "❌ Consistency check failed. Aborting commit."
    exit 1
fi
```

#### CI/CD Integration
Add to GitHub Actions or other CI systems:
```yaml
- name: Run consistency check
  run: |
    python3 tools/consistency-checker.py
    if [ $? -ne 0 ]; then
      echo "❌ Consistency check failed"
      exit 1
    fi
```

#### Build Process Integration
Update your build scripts to include consistency checking:
```bash
# Before building
./scripts/consistency-check.sh

# Build only if check passes
if [ $? -eq 0 ]; then
    hugo --gc --minify
fi
```

### Issue Types

The checker identifies these issue types:

#### Errors (Block Deployment)
- **broken_internal_link**: Internal links that don't point to existing pages
- **missing_required_field**: Front matter missing required fields (e.g., title)
- **duplicate_header**: Duplicate H1 headers in the same file
- **missing_index**: Directories without _index.md files

#### Warnings (Should Fix)
- **multiple_h1**: Multiple H1 headers in one file (should typically have one)
- **navigation_override**: Pages that override global navigation
- **missing_front_matter**: Files without front matter
- **missing_section**: Expected top-level sections that are missing

#### Info (Nice to Have)
- **layout_override**: Pages with custom layouts
- **unexpected_section**: Top-level sections not in expected list

### Configuration

The tool uses these configuration constants:

```python
EXPECTED_SECTIONS = {
    'user-guide', 'modules', 'applets', 'developers', 'api-reference',
    'business-operations', 'tutorials', 'guides', 'industry-solutions',
    'support', 'applications'
}
```

To modify expected sections, edit the `EXPECTED_SECTIONS` set in the script.

### Report Format

The JSON report includes:

```json
{
  "timestamp": "2025-08-26T10:57:04.892854",
  "total_files_checked": 200,
  "file_structure": {
    "applets/": 52,
    "modules/": 33,
    "user-guide/": 29
  },
  "issues": [
    {
      "type": "broken_internal_link",
      "severity": "error",
      "file_path": "_index.md",
      "line_number": 46,
      "message": "Broken internal link: /user-guide/introduction/",
      "details": {"link": "/user-guide/introduction/", "normalized": "/user-guide/introduction/"}
    }
  ],
  "todos": [
    {
      "file": "applets/example.md",
      "line": 10,
      "type": "TODO",
      "text": "Add more examples",
      "full_line": "<!-- TODO: Add more examples -->"
    }
  ],
  "summary": {
    "total_issues": 387,
    "errors": 360,
    "warnings": 20,
    "info": 7,
    "todos": 423
  }
}
```

## Other Tools

- **check_links.py**: Alternative link checker
- **fix_broken_links.py**: Automated link fixing (use with caution)

## Dependencies

The consistency checker uses only built-in Python modules:
- `pathlib` - File system operations
- `re` - Regular expressions
- `json` - JSON handling
- `dataclasses` - Data structures
- `argparse` - Command line parsing
- `datetime` - Timestamps

No external dependencies required!