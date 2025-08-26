#!/usr/bin/env python3
"""
BigLedger Wiki Consistency Checker

This script ensures the BigLedger wiki maintains quality standards by checking:
1. Navigation consistency across all pages
2. No duplicate H1 headers in markdown files
3. No broken internal links
4. Proper file structure
5. Front matter validation
6. TODO tracking

Usage:
    python consistency-checker.py
    python consistency-checker.py --report-only
    python consistency-checker.py --fix-issues
"""

import os
import re
import sys
import argparse
from pathlib import Path
from typing import Dict, List, Set, Tuple, Optional, Any
from dataclasses import dataclass, field
from datetime import datetime
import json

# Configuration
CONTENT_DIR = Path("content/en")
HUGO_CONFIG = Path("hugo.yaml")
REPORT_FILE = Path("consistency-report.json")
EXPECTED_SECTIONS = {
    'user-guide', 'modules', 'applets', 'developers', 'api-reference',
    'business-operations', 'tutorials', 'guides', 'industry-solutions',
    'support', 'applications'
}

@dataclass
class Issue:
    """Represents a consistency issue found in the documentation"""
    type: str
    severity: str  # 'error', 'warning', 'info'
    file_path: str
    line_number: Optional[int] = None
    message: str = ""
    details: Dict[str, Any] = field(default_factory=dict)

@dataclass
class ConsistencyReport:
    """Complete consistency check report"""
    timestamp: str
    total_files_checked: int
    issues: List[Issue] = field(default_factory=list)
    navigation_structure: Dict[str, Any] = field(default_factory=dict)
    todos: List[Dict[str, Any]] = field(default_factory=list)
    file_structure: Dict[str, int] = field(default_factory=dict)
    
    def add_issue(self, issue: Issue):
        self.issues.append(issue)
    
    def get_issues_by_type(self, issue_type: str) -> List[Issue]:
        return [issue for issue in self.issues if issue.type == issue_type]
    
    def get_issues_by_severity(self, severity: str) -> List[Issue]:
        return [issue for issue in self.issues if issue.severity == severity]

class ConsistencyChecker:
    """Main consistency checker class"""
    
    def __init__(self, content_dir: Path, hugo_config: Path):
        self.content_dir = content_dir
        self.hugo_config = hugo_config
        self.report = ConsistencyReport(
            timestamp=datetime.now().isoformat(),
            total_files_checked=0
        )
        self.navigation_menu = {}
        self.all_pages = set()
        self.markdown_files = []
        
    def run_all_checks(self) -> ConsistencyReport:
        """Run all consistency checks"""
        print("🔍 BigLedger Wiki Consistency Checker")
        print("=" * 50)
        
        try:
            # Initialize
            self._load_hugo_config()
            self._collect_markdown_files()
            self._collect_all_pages()
            
            # Run all checks
            print("\n📋 Running consistency checks...")
            self._check_navigation_consistency()
            self._check_duplicate_headers()
            self._check_broken_internal_links()
            self._check_file_structure()
            self._check_front_matter_validation()
            self._track_todos()
            
            # Generate statistics
            self.report.total_files_checked = len(self.markdown_files)
            self.report.file_structure = self._get_file_structure_stats()
            
            print(f"\n✅ Consistency check complete!")
            print(f"📊 Files checked: {self.report.total_files_checked}")
            print(f"⚠️  Issues found: {len(self.report.issues)}")
            
            return self.report
            
        except Exception as e:
            self.report.add_issue(Issue(
                type="system_error",
                severity="error",
                file_path="system",
                message=f"Consistency checker failed: {str(e)}"
            ))
            return self.report
    
    def _load_hugo_config(self):
        """Load Hugo configuration"""
        try:
            with open(self.hugo_config, 'r', encoding='utf-8') as f:
                content = f.read()
                # Simple parsing - just look for menu items
                menu_items = []
                in_menu_section = False
                
                for line in content.split('\n'):
                    line = line.strip()
                    if line.startswith('menu:'):
                        in_menu_section = True
                        continue
                    elif line and not line.startswith(' ') and not line.startswith('-') and in_menu_section:
                        in_menu_section = False
                    
                    if in_menu_section and line.startswith('- identifier:'):
                        identifier = line.split(':', 1)[1].strip()
                        menu_items.append({'identifier': identifier})
                
                self.navigation_menu = {'main': menu_items}
            print(f"✅ Loaded Hugo configuration from {self.hugo_config}")
        except Exception as e:
            self.report.add_issue(Issue(
                type="config_error",
                severity="error",
                file_path=str(self.hugo_config),
                message=f"Failed to load Hugo config: {str(e)}"
            ))
    
    def _collect_markdown_files(self):
        """Collect all markdown files"""
        self.markdown_files = list(self.content_dir.rglob("*.md"))
        print(f"📁 Found {len(self.markdown_files)} markdown files")
    
    def _collect_all_pages(self):
        """Collect all page URLs for link validation"""
        for md_file in self.markdown_files:
            relative_path = md_file.relative_to(self.content_dir)
            if md_file.name == "_index.md":
                # Directory index page
                page_url = "/" + str(relative_path.parent) + "/"
                if page_url == "/./" or page_url == "/./":
                    page_url = "/"
            else:
                # Regular page
                page_url = "/" + str(relative_path.with_suffix("")) + "/"
            
            self.all_pages.add(page_url)
            # Also add without trailing slash
            self.all_pages.add(page_url.rstrip("/"))
    
    def _check_navigation_consistency(self):
        """Check navigation consistency across pages"""
        print("🧭 Checking navigation consistency...")
        
        expected_nav_items = {item['identifier']: item for item in self.navigation_menu.get('main', [])}
        
        for md_file in self.markdown_files:
            try:
                content = md_file.read_text(encoding='utf-8')
                front_matter, _ = self._parse_front_matter(content)
                
                if front_matter and 'menu' in front_matter:
                    # Check if page overrides navigation
                    self.report.add_issue(Issue(
                        type="navigation_override",
                        severity="warning",
                        file_path=str(md_file.relative_to(self.content_dir)),
                        message="Page overrides global navigation menu"
                    ))
                
            except Exception as e:
                self.report.add_issue(Issue(
                    type="navigation_check_error",
                    severity="error",
                    file_path=str(md_file.relative_to(self.content_dir)),
                    message=f"Error checking navigation: {str(e)}"
                ))
        
        self.report.navigation_structure = expected_nav_items
    
    def _check_duplicate_headers(self):
        """Check for duplicate H1 headers in markdown files"""
        print("📝 Checking for duplicate H1 headers...")
        
        for md_file in self.markdown_files:
            try:
                content = md_file.read_text(encoding='utf-8')
                lines = content.split('\n')
                
                h1_headers = []
                for i, line in enumerate(lines, 1):
                    # Check for markdown H1 headers
                    if line.strip().startswith('# '):
                        h1_headers.append((i, line.strip()))
                
                # Check for duplicates
                header_texts = [header[1] for header in h1_headers]
                seen_headers = set()
                for line_num, header_text in h1_headers:
                    if header_text in seen_headers:
                        self.report.add_issue(Issue(
                            type="duplicate_header",
                            severity="error",
                            file_path=str(md_file.relative_to(self.content_dir)),
                            line_number=line_num,
                            message=f"Duplicate H1 header: {header_text}",
                            details={'header': header_text}
                        ))
                    else:
                        seen_headers.add(header_text)
                
                # Check for multiple H1s (should typically be only one main heading)
                if len(h1_headers) > 1:
                    self.report.add_issue(Issue(
                        type="multiple_h1",
                        severity="warning",
                        file_path=str(md_file.relative_to(self.content_dir)),
                        message=f"Multiple H1 headers found ({len(h1_headers)})",
                        details={'count': len(h1_headers), 'headers': header_texts}
                    ))
                        
            except Exception as e:
                self.report.add_issue(Issue(
                    type="header_check_error",
                    severity="error",
                    file_path=str(md_file.relative_to(self.content_dir)),
                    message=f"Error checking headers: {str(e)}"
                ))
    
    def _check_broken_internal_links(self):
        """Check for broken internal links"""
        print("🔗 Checking for broken internal links...")
        
        # Link patterns to find
        link_patterns = [
            r'\[([^\]]*)\]\(([^)]+)\)',  # Markdown links
            r'{{<\s*card\s+link="([^"]+)"',  # Hugo card shortcodes
            r'pageRef:\s*([^\s]+)',  # Hugo menu pageRef
        ]
        
        for md_file in self.markdown_files:
            try:
                content = md_file.read_text(encoding='utf-8')
                lines = content.split('\n')
                
                for i, line in enumerate(lines, 1):
                    for pattern in link_patterns:
                        matches = re.finditer(pattern, line)
                        for match in matches:
                            if pattern.startswith(r'\['):
                                # Markdown link - extract URL from second group
                                link_url = match.group(2)
                            else:
                                # Other patterns - extract URL from first group
                                link_url = match.group(1)
                            
                            # Skip external links
                            if self._is_external_link(link_url):
                                continue
                            
                            # Normalize the link
                            normalized_link = self._normalize_internal_link(link_url)
                            
                            # Check if link target exists
                            if not self._link_target_exists(normalized_link):
                                self.report.add_issue(Issue(
                                    type="broken_internal_link",
                                    severity="error",
                                    file_path=str(md_file.relative_to(self.content_dir)),
                                    line_number=i,
                                    message=f"Broken internal link: {link_url}",
                                    details={'link': link_url, 'normalized': normalized_link}
                                ))
                        
            except Exception as e:
                self.report.add_issue(Issue(
                    type="link_check_error",
                    severity="error",
                    file_path=str(md_file.relative_to(self.content_dir)),
                    message=f"Error checking links: {str(e)}"
                ))
    
    def _check_file_structure(self):
        """Check proper file structure adherence"""
        print("📂 Checking file structure...")
        
        # Check if all expected sections exist
        existing_sections = set()
        for md_file in self.markdown_files:
            relative_path = md_file.relative_to(self.content_dir)
            if len(relative_path.parts) > 0:
                top_level = relative_path.parts[0]
                if top_level != "_index.md":  # Skip root index
                    existing_sections.add(top_level)
        
        # Check for missing expected sections
        missing_sections = EXPECTED_SECTIONS - existing_sections
        for section in missing_sections:
            self.report.add_issue(Issue(
                type="missing_section",
                severity="warning",
                file_path="structure",
                message=f"Missing expected section: {section}",
                details={'section': section}
            ))
        
        # Check for unexpected top-level directories
        unexpected_sections = existing_sections - EXPECTED_SECTIONS
        for section in unexpected_sections:
            self.report.add_issue(Issue(
                type="unexpected_section",
                severity="info",
                file_path="structure",
                message=f"Unexpected top-level section: {section}",
                details={'section': section}
            ))
        
        # Check that each directory has an _index.md file
        for section in existing_sections:
            index_file = self.content_dir / section / "_index.md"
            if not index_file.exists():
                self.report.add_issue(Issue(
                    type="missing_index",
                    severity="error",
                    file_path=f"{section}/",
                    message=f"Missing _index.md file in {section} directory"
                ))
    
    def _check_front_matter_validation(self):
        """Check front matter validation"""
        print("📋 Checking front matter validation...")
        
        required_fields = {'title'}  # Common required fields
        recommended_fields = {'description', 'weight'}  # Recommended fields
        
        for md_file in self.markdown_files:
            try:
                content = md_file.read_text(encoding='utf-8')
                front_matter, _ = self._parse_front_matter(content)
                
                if not front_matter:
                    self.report.add_issue(Issue(
                        type="missing_front_matter",
                        severity="warning",
                        file_path=str(md_file.relative_to(self.content_dir)),
                        message="No front matter found"
                    ))
                    continue
                
                # Check required fields
                for field in required_fields:
                    if field not in front_matter:
                        self.report.add_issue(Issue(
                            type="missing_required_field",
                            severity="error",
                            file_path=str(md_file.relative_to(self.content_dir)),
                            message=f"Missing required front matter field: {field}",
                            details={'field': field}
                        ))
                
                # Check for navigation override (should be rare)
                if 'menu' in front_matter:
                    self.report.add_issue(Issue(
                        type="front_matter_menu_override",
                        severity="warning",
                        file_path=str(md_file.relative_to(self.content_dir)),
                        message="Front matter overrides navigation menu"
                    ))
                
                # Check for layout overrides
                if 'layout' in front_matter and front_matter['layout'] != 'hextra-home':
                    self.report.add_issue(Issue(
                        type="layout_override",
                        severity="info",
                        file_path=str(md_file.relative_to(self.content_dir)),
                        message=f"Custom layout specified: {front_matter['layout']}",
                        details={'layout': front_matter['layout']}
                    ))
                        
            except Exception as e:
                self.report.add_issue(Issue(
                    type="front_matter_error",
                    severity="error",
                    file_path=str(md_file.relative_to(self.content_dir)),
                    message=f"Error parsing front matter: {str(e)}"
                ))
    
    def _track_todos(self):
        """Track TODO markers for incomplete content"""
        print("📝 Tracking TODO markers...")
        
        todo_patterns = [
            r'TODO:?\s*(.+)',
            r'FIXME:?\s*(.+)',
            r'HACK:?\s*(.+)',
            r'XXX:?\s*(.+)',
            r'NOTE:?\s*(.+)',
            r'<!--\s*TODO:?\s*(.+?)\s*-->',  # HTML comments
        ]
        
        for md_file in self.markdown_files:
            try:
                content = md_file.read_text(encoding='utf-8')
                lines = content.split('\n')
                
                for i, line in enumerate(lines, 1):
                    for pattern in todo_patterns:
                        matches = re.finditer(pattern, line, re.IGNORECASE)
                        for match in matches:
                            todo_text = match.group(1).strip() if len(match.groups()) > 0 else line.strip()
                            
                            self.report.todos.append({
                                'file': str(md_file.relative_to(self.content_dir)),
                                'line': i,
                                'type': pattern.split(':')[0].upper().replace('R',''),
                                'text': todo_text,
                                'full_line': line.strip()
                            })
                        
            except Exception as e:
                self.report.add_issue(Issue(
                    type="todo_tracking_error",
                    severity="error",
                    file_path=str(md_file.relative_to(self.content_dir)),
                    message=f"Error tracking TODOs: {str(e)}"
                ))
    
    def _parse_front_matter(self, content: str) -> Tuple[Optional[Dict], str]:
        """Parse YAML front matter from markdown content"""
        if not content.startswith('---'):
            return None, content
        
        try:
            # Find the end of front matter
            end_marker = content.find('\n---\n', 3)
            if end_marker == -1:
                return None, content
            
            # Extract front matter
            front_matter_str = content[3:end_marker]
            body = content[end_marker + 5:]
            
            # Simple YAML parsing - just key-value pairs
            front_matter = {}
            for line in front_matter_str.split('\n'):
                line = line.strip()
                if line and ':' in line and not line.startswith('#'):
                    key, value = line.split(':', 1)
                    key = key.strip()
                    value = value.strip().strip('"\'')
                    if value.lower() in ('true', 'false'):
                        value = value.lower() == 'true'
                    elif value.isdigit():
                        value = int(value)
                    front_matter[key] = value
            
            return front_matter, body
            
        except Exception:
            return None, content
    
    def _is_external_link(self, link: str) -> bool:
        """Check if a link is external"""
        return (link.startswith('http://') or 
                link.startswith('https://') or 
                link.startswith('mailto:') or
                link.startswith('tel:') or
                link.startswith('ftp://'))
    
    def _normalize_internal_link(self, link: str) -> str:
        """Normalize internal link for consistency"""
        # Remove fragments
        if '#' in link:
            link = link.split('#')[0]
        
        # Ensure starts with /
        if not link.startswith('/'):
            link = '/' + link
        
        # Normalize trailing slashes
        if not link.endswith('/') and '.' not in link.split('/')[-1]:
            link = link + '/'
        
        return link
    
    def _link_target_exists(self, link: str) -> bool:
        """Check if the link target exists"""
        # Normalize for comparison
        link = link.rstrip('/') if link != '/' else link
        
        # Check in our collected pages
        for page in self.all_pages:
            if page == link or page == link + '/':
                return True
        
        # Check for actual file existence
        if link.startswith('/'):
            # Try as directory with _index.md
            dir_path = self.content_dir / link[1:]
            if (dir_path / "_index.md").exists():
                return True
            
            # Try as markdown file
            md_path = self.content_dir / (link[1:] + ".md")
            if md_path.exists():
                return True
        
        return False
    
    def _get_file_structure_stats(self) -> Dict[str, int]:
        """Get file structure statistics"""
        stats = {}
        
        for md_file in self.markdown_files:
            relative_path = md_file.relative_to(self.content_dir)
            if len(relative_path.parts) > 0:
                section = relative_path.parts[0]
                if section == "_index.md":
                    section = "root"
                stats[section] = stats.get(section, 0) + 1
        
        return stats

def print_report(report: ConsistencyReport, verbose: bool = False):
    """Print the consistency report to console"""
    print(f"\n📊 CONSISTENCY REPORT")
    print("=" * 50)
    print(f"Timestamp: {report.timestamp}")
    print(f"Files checked: {report.total_files_checked}")
    print(f"Total issues: {len(report.issues)}")
    print(f"TODOs found: {len(report.todos)}")
    
    # Issue summary by type
    issue_types = {}
    severity_counts = {'error': 0, 'warning': 0, 'info': 0}
    
    for issue in report.issues:
        issue_types[issue.type] = issue_types.get(issue.type, 0) + 1
        severity_counts[issue.severity] += 1
    
    print(f"\n📋 ISSUE SUMMARY:")
    print(f"  Errors: {severity_counts['error']}")
    print(f"  Warnings: {severity_counts['warning']}")  
    print(f"  Info: {severity_counts['info']}")
    
    if issue_types:
        print(f"\n🔍 ISSUE TYPES:")
        for issue_type, count in sorted(issue_types.items()):
            print(f"  {issue_type}: {count}")
    
    # File structure
    if report.file_structure:
        print(f"\n📂 FILE STRUCTURE:")
        for section, count in sorted(report.file_structure.items()):
            print(f"  {section}/: {count} files")
    
    # TODOs summary
    if report.todos:
        print(f"\n📝 TODO SUMMARY:")
        todo_types = {}
        for todo in report.todos:
            todo_type = todo['type']
            todo_types[todo_type] = todo_types.get(todo_type, 0) + 1
        
        for todo_type, count in sorted(todo_types.items()):
            print(f"  {todo_type}: {count}")
    
    # Detailed issues (if verbose or critical errors)
    errors = report.get_issues_by_severity('error')
    if errors and (verbose or len(errors) <= 20):
        print(f"\n🚨 ERRORS:")
        for issue in errors[:20]:  # Limit to first 20
            print(f"  📍 {issue.file_path}:{issue.line_number or 'N/A'}")
            print(f"     {issue.message}")
    
    # Show some TODOs if not too many
    if report.todos and len(report.todos) <= 10:
        print(f"\n📝 TODOS:")
        for todo in report.todos:
            print(f"  📍 {todo['file']}:{todo['line']}")
            print(f"     {todo['type']}: {todo['text']}")

def save_report(report: ConsistencyReport, output_file: Path):
    """Save the report to JSON file"""
    report_data = {
        'timestamp': report.timestamp,
        'total_files_checked': report.total_files_checked,
        'file_structure': report.file_structure,
        'navigation_structure': report.navigation_structure,
        'issues': [
            {
                'type': issue.type,
                'severity': issue.severity,
                'file_path': issue.file_path,
                'line_number': issue.line_number,
                'message': issue.message,
                'details': issue.details
            }
            for issue in report.issues
        ],
        'todos': report.todos,
        'summary': {
            'total_issues': len(report.issues),
            'errors': len(report.get_issues_by_severity('error')),
            'warnings': len(report.get_issues_by_severity('warning')),
            'info': len(report.get_issues_by_severity('info')),
            'todos': len(report.todos)
        }
    }
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(report_data, f, indent=2, ensure_ascii=False)
    
    print(f"📄 Report saved to: {output_file}")

def main():
    """Main function"""
    parser = argparse.ArgumentParser(description='BigLedger Wiki Consistency Checker')
    parser.add_argument('--report-only', action='store_true', 
                       help='Only generate report, do not suggest fixes')
    parser.add_argument('--verbose', '-v', action='store_true',
                       help='Show detailed output')
    parser.add_argument('--output', '-o', default='consistency-report.json',
                       help='Output file for detailed report')
    parser.add_argument('--content-dir', default='content/en',
                       help='Content directory to check')
    parser.add_argument('--config', default='hugo.yaml',
                       help='Hugo configuration file')
    
    args = parser.parse_args()
    
    # Validate paths
    content_dir = Path(args.content_dir)
    hugo_config = Path(args.config)
    
    if not content_dir.exists():
        print(f"❌ Content directory not found: {content_dir}")
        sys.exit(1)
    
    if not hugo_config.exists():
        print(f"❌ Hugo config not found: {hugo_config}")
        sys.exit(1)
    
    # Run consistency check
    checker = ConsistencyChecker(content_dir, hugo_config)
    report = checker.run_all_checks()
    
    # Print report
    print_report(report, args.verbose)
    
    # Save detailed report
    output_file = Path(args.output)
    save_report(report, output_file)
    
    # Exit with appropriate code
    error_count = len(report.get_issues_by_severity('error'))
    if error_count > 0:
        print(f"\n❌ Found {error_count} errors. Please fix them before deployment.")
        sys.exit(1)
    else:
        print(f"\n✅ No critical errors found!")
        sys.exit(0)

if __name__ == "__main__":
    main()