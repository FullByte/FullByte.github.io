#!/usr/bin/env python3
"""
Simple MkDocs Site Tester
Tests the built MkDocs site for basic functionality and issues
"""

import os
import json
import time
import argparse
from pathlib import Path
from urllib.parse import urljoin, urlparse
import re
from collections import defaultdict
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class SimpleSiteTester:
    def __init__(self, site_dir: str):
        self.site_dir = Path(site_dir)
        if not self.site_dir.exists():
            raise ValueError(f"Site directory {site_dir} does not exist")
        
        self.results = {}
        self.issues = []
        self.total_files = 0
        self.html_files = []
        
    def find_html_files(self):
        """Find all HTML files in the site directory."""
        self.html_files = list(self.site_dir.rglob("*.html"))
        self.total_files = len(self.html_files)
        logger.info(f"Found {self.total_files} HTML files")
        
    def analyze_html_file(self, file_path: Path) -> dict:
        """Analyze a single HTML file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            return {'error': f"Failed to read file: {e}"}
        
        analysis = {
            'file_path': str(file_path.relative_to(self.site_dir)),
            'file_size_kb': file_path.stat().st_size / 1024,
            'issues': [],
            'warnings': [],
            'info': {}
        }
        
        # Basic HTML structure checks
        if '<html' not in content.lower():
            analysis['issues'].append('Missing HTML tag')
        
        if '<head>' not in content.lower():
            analysis['issues'].append('Missing HEAD section')
            
        if '<body>' not in content.lower():
            analysis['issues'].append('Missing BODY section')
        
        # Title check
        title_match = re.search(r'<title[^>]*>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
        if title_match:
            title = title_match.group(1).strip()
            analysis['info']['title'] = title
            if not title:
                analysis['issues'].append('Empty title tag')
            elif len(title) > 60:
                analysis['warnings'].append(f'Title too long ({len(title)} chars)')
        else:
            analysis['issues'].append('Missing title tag')
        
        # Meta description check
        meta_desc_match = re.search(r'<meta[^>]*name=["\']description["\'][^>]*content=["\']([^"\']*)["\']', content, re.IGNORECASE)
        if meta_desc_match:
            description = meta_desc_match.group(1).strip()
            analysis['info']['meta_description'] = description
            if not description:
                analysis['warnings'].append('Empty meta description')
            elif len(description) > 160:
                analysis['warnings'].append(f'Meta description too long ({len(description)} chars)')
        else:
            analysis['warnings'].append('Missing meta description')
        
        # Heading structure
        h1_matches = re.findall(r'<h1[^>]*>', content, re.IGNORECASE)
        h2_matches = re.findall(r'<h2[^>]*>', content, re.IGNORECASE)
        h3_matches = re.findall(r'<h3[^>]*>', content, re.IGNORECASE)
        
        analysis['info']['h1_count'] = len(h1_matches)
        analysis['info']['h2_count'] = len(h2_matches)
        analysis['info']['h3_count'] = len(h3_matches)
        
        if len(h1_matches) == 0:
            analysis['warnings'].append('No H1 heading found')
        elif len(h1_matches) > 1:
            analysis['warnings'].append(f'Multiple H1 headings ({len(h1_matches)})')
        
        # Image checks
        img_matches = re.findall(r'<img[^>]*>', content, re.IGNORECASE)
        img_without_alt = re.findall(r'<img(?![^>]*alt=)[^>]*>', content, re.IGNORECASE)
        
        analysis['info']['total_images'] = len(img_matches)
        analysis['info']['images_without_alt'] = len(img_without_alt)
        
        if len(img_without_alt) > 0:
            analysis['warnings'].append(f'{len(img_without_alt)} images without alt text')
        
        # Link checks (internal)
        link_matches = re.findall(r'<a[^>]*href=["\']([^"\']*)["\'][^>]*>', content, re.IGNORECASE)
        internal_links = []
        external_links = []
        
        for link in link_matches:
            if link.startswith('http://') or link.startswith('https://'):
                external_links.append(link)
            elif link.startswith('#'):
                # Fragment link - skip for now
                continue
            else:
                internal_links.append(link)
        
        analysis['info']['internal_links'] = len(internal_links)
        analysis['info']['external_links'] = len(external_links)
        
        # Check for broken internal links
        broken_internal = []
        for link in internal_links:
            if link.startswith('/'):
                # Absolute path
                link_path = self.site_dir / link.lstrip('/')
                if link.endswith('/'):
                    link_path = link_path / 'index.html'
                elif not link.endswith('.html'):
                    link_path = link_path / 'index.html'
            else:
                # Relative path
                link_path = file_path.parent / link
                if link.endswith('/'):
                    link_path = link_path / 'index.html'
                elif not link.endswith('.html') and '.' not in link:
                    link_path = link_path / 'index.html'
            
            try:
                resolved_path = link_path.resolve()
                if not resolved_path.exists():
                    broken_internal.append(link)
            except:
                broken_internal.append(link)
        
        if broken_internal:
            analysis['issues'].extend([f'Broken internal link: {link}' for link in broken_internal])
        
        # File size warnings
        if analysis['file_size_kb'] > 500:
            analysis['warnings'].append(f'Large file size: {analysis["file_size_kb"]:.1f}KB')
        
        # Check for WebP image usage
        webp_images = re.findall(r'src=["\'][^"\']*\.webp["\']', content, re.IGNORECASE)
        old_format_images = re.findall(r'src=["\'][^"\']*\.(jpg|jpeg|png)["\']', content, re.IGNORECASE)
        
        if old_format_images:
            analysis['warnings'].append(f'{len(old_format_images)} non-WebP images found')
        
        analysis['info']['webp_images'] = len(webp_images)
        analysis['info']['old_format_images'] = len(old_format_images)
        
        return analysis
    
    def check_site_structure(self):
        """Check overall site structure."""
        structure_issues = []
        
        # Check for essential files
        essential_files = ['index.html', 'sitemap.xml', 'robots.txt']
        for file in essential_files:
            if not (self.site_dir / file).exists():
                structure_issues.append(f'Missing {file}')
        
        # Check for 404 page
        if not (self.site_dir / '404.html').exists():
            structure_issues.append('Missing 404.html')
        
        # Check for assets directory
        assets_dir = self.site_dir / 'assets'
        if not assets_dir.exists():
            structure_issues.append('Missing assets directory')
        
        # Check for search functionality
        search_files = list(self.site_dir.rglob('*search*'))
        if not search_files:
            structure_issues.append('No search functionality detected')
        
        return structure_issues
    
    def run_tests(self):
        """Run all tests on the site."""
        logger.info("Starting site tests...")
        
        # Find all HTML files
        self.find_html_files()
        
        # Test each HTML file
        for i, html_file in enumerate(self.html_files, 1):
            logger.info(f"Testing {html_file.name} ({i}/{self.total_files})")
            result = self.analyze_html_file(html_file)
            self.results[str(html_file.relative_to(self.site_dir))] = result
            
            # Collect issues
            if 'issues' in result:
                for issue in result['issues']:
                    self.issues.append((str(html_file.relative_to(self.site_dir)), issue))
        
        # Check site structure
        structure_issues = self.check_site_structure()
        for issue in structure_issues:
            self.issues.append(('site_structure', issue))
        
        return self.generate_report()
    
    def generate_report(self):
        """Generate test report."""
        total_issues = len(self.issues)
        total_warnings = sum(len(result.get('warnings', [])) for result in self.results.values())
        
        # Categorize issues
        issue_categories = defaultdict(int)
        for _, issue in self.issues:
            if 'missing' in issue.lower():
                issue_categories['Missing Elements'] += 1
            elif 'broken' in issue.lower():
                issue_categories['Broken Links'] += 1
            elif 'empty' in issue.lower():
                issue_categories['Empty Content'] += 1
            else:
                issue_categories['Other'] += 1
        
        # Performance stats
        file_sizes = [result['file_size_kb'] for result in self.results.values() if 'file_size_kb' in result]
        avg_file_size = sum(file_sizes) / len(file_sizes) if file_sizes else 0
        max_file_size = max(file_sizes) if file_sizes else 0
        
        # Image optimization stats
        total_webp = sum(result.get('info', {}).get('webp_images', 0) for result in self.results.values())
        total_old_format = sum(result.get('info', {}).get('old_format_images', 0) for result in self.results.values())
        
        report = {
            'summary': {
                'total_files_tested': self.total_files,
                'total_issues': total_issues,
                'total_warnings': total_warnings,
                'test_passed': total_issues == 0,
                'site_directory': str(self.site_dir)
            },
            'performance': {
                'average_file_size_kb': avg_file_size,
                'max_file_size_kb': max_file_size,
                'large_files': [f for f, result in self.results.items() 
                              if result.get('file_size_kb', 0) > 500]
            },
            'images': {
                'total_webp_images': total_webp,
                'total_old_format_images': total_old_format,
                'optimization_ratio': (total_webp / (total_webp + total_old_format) * 100) if (total_webp + total_old_format) > 0 else 100
            },
            'issues': {
                'by_category': dict(issue_categories),
                'all_issues': self.issues
            },
            'detailed_results': self.results
        }
        
        return report
    
    def save_report(self, report: dict, output_file: str):
        """Save report to JSON file."""
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        logger.info(f"Report saved to {output_file}")
    
    def print_summary(self, report: dict):
        """Print summary to console."""
        summary = report['summary']
        performance = report['performance']
        images = report['images']
        issues = report['issues']
        
        print("\n" + "="*50)
        print("SITE TEST SUMMARY")
        print("="*50)
        print(f"Site Directory: {summary['site_directory']}")
        print(f"Files Tested: {summary['total_files_tested']}")
        print(f"Total Issues: {summary['total_issues']}")
        print(f"Total Warnings: {summary['total_warnings']}")
        print(f"Test Status: {'PASSED' if summary['test_passed'] else 'FAILED'}")
        
        print("\n" + "-"*30)
        print("PERFORMANCE")
        print("-"*30)
        print(f"Average File Size: {performance['average_file_size_kb']:.1f}KB")
        print(f"Largest File: {performance['max_file_size_kb']:.1f}KB")
        if performance['large_files']:
            print(f"Large Files (>500KB): {len(performance['large_files'])}")
        
        print("\n" + "-"*30)
        print("IMAGE OPTIMIZATION")
        print("-"*30)
        print(f"WebP Images: {images['total_webp_images']}")
        print(f"Old Format Images: {images['total_old_format_images']}")
        print(f"Optimization Ratio: {images['optimization_ratio']:.1f}%")
        
        print("\n" + "-"*30)
        print("ISSUES BY CATEGORY")
        print("-"*30)
        for category, count in issues['by_category'].items():
            print(f"{category}: {count}")
        
        if issues['all_issues']:
            print("\n" + "-"*30)
            print("SAMPLE ISSUES")
            print("-"*30)
            for file, issue in issues['all_issues'][:10]:  # Show first 10
                print(f"{file}: {issue}")
        
        print("\n" + "="*50)

def main():
    parser = argparse.ArgumentParser(description="Test MkDocs built site")
    parser.add_argument("--site-dir", default="site", help="Path to built site directory")
    parser.add_argument("--output", default="site_test_report.json", help="Output file for report")
    parser.add_argument("--quiet", action="store_true", help="Suppress console output")
    
    args = parser.parse_args()
    
    if args.quiet:
        logging.getLogger().setLevel(logging.WARNING)
    
    try:
        tester = SimpleSiteTester(args.site_dir)
        report = tester.run_tests()
        
        # Save report
        tester.save_report(report, args.output)
        
        # Print summary
        if not args.quiet:
            tester.print_summary(report)
        
        # Return appropriate exit code
        if not report['summary']['test_passed']:
            return 1
        else:
            return 0
            
    except Exception as e:
        logger.error(f"Test failed: {e}")
        return 1

if __name__ == "__main__":
    exit(main())
