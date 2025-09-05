#!/usr/bin/env python3
"""
MkDocs Site Crawler and Tester
Crawls and tests all pages of the MkDocs site for functionality, performance, and issues
"""

import os
import sys
import json
import time
import asyncio
import aiohttp
import argparse
from pathlib import Path
from urllib.parse import urljoin, urlparse, unquote
from bs4 import BeautifulSoup
from collections import defaultdict
import logging
from typing import Dict, List, Set, Tuple, Optional
import re

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class SiteCrawler:
    def __init__(self, base_url: str, max_pages: int = None, delay: float = 0.5):
        self.base_url = base_url.rstrip('/')
        self.domain = urlparse(base_url).netloc
        self.max_pages = max_pages
        self.delay = delay
        
        # Track crawled URLs and results
        self.crawled_urls: Set[str] = set()
        self.to_crawl: Set[str] = {base_url}
        self.results: Dict[str, Dict] = {}
        self.broken_links: List[Tuple[str, str, int]] = []
        self.images: List[Tuple[str, str, int]] = []
        self.external_links: List[Tuple[str, str]] = []
        
        # Performance tracking
        self.total_start_time = time.time()
        self.page_timings: Dict[str, float] = {}

    async def fetch_page(self, session: aiohttp.ClientSession, url: str) -> Tuple[str, int, str, float]:
        """Fetch a single page and return content, status code, and timing."""
        start_time = time.time()
        try:
            async with session.get(url, timeout=aiohttp.ClientTimeout(total=30)) as response:
                content = await response.text()
                load_time = time.time() - start_time
                return content, response.status, str(response.url), load_time
        except asyncio.TimeoutError:
            load_time = time.time() - start_time
            logger.warning(f"Timeout loading {url}")
            return "", 408, url, load_time
        except Exception as e:
            load_time = time.time() - start_time
            logger.error(f"Error loading {url}: {e}")
            return "", 500, url, load_time

    def extract_links(self, content: str, base_url: str) -> Tuple[List[str], List[str], List[str]]:
        """Extract internal links, external links, and images from page content."""
        soup = BeautifulSoup(content, 'html.parser')
        
        internal_links = []
        external_links = []
        images = []
        
        # Extract links
        for link in soup.find_all('a', href=True):
            href = link['href']
            full_url = urljoin(base_url, href)
            parsed = urlparse(full_url)
            
            if parsed.netloc == self.domain or not parsed.netloc:
                # Internal link
                clean_url = full_url.split('#')[0]  # Remove fragment
                if clean_url not in self.crawled_urls and clean_url.startswith(self.base_url):
                    internal_links.append(clean_url)
            else:
                # External link
                external_links.append(full_url)
        
        # Extract images
        for img in soup.find_all('img', src=True):
            src = img['src']
            full_url = urljoin(base_url, src)
            images.append(full_url)
            
        return internal_links, external_links, images

    def analyze_page_content(self, content: str, url: str) -> Dict:
        """Analyze page content for SEO, accessibility, and other metrics."""
        soup = BeautifulSoup(content, 'html.parser')
        
        analysis = {
            'title': None,
            'meta_description': None,
            'h1_count': 0,
            'h2_count': 0,
            'h3_count': 0,
            'img_without_alt': 0,
            'total_images': 0,
            'total_links': 0,
            'word_count': 0,
            'has_schema_markup': False,
            'page_size_kb': len(content.encode('utf-8')) / 1024,
            'issues': []
        }
        
        # Title
        title_tag = soup.find('title')
        if title_tag:
            analysis['title'] = title_tag.get_text().strip()
        else:
            analysis['issues'].append('Missing title tag')
            
        # Meta description
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        if meta_desc:
            analysis['meta_description'] = meta_desc.get('content', '').strip()
        else:
            analysis['issues'].append('Missing meta description')
            
        # Headings
        analysis['h1_count'] = len(soup.find_all('h1'))
        analysis['h2_count'] = len(soup.find_all('h2'))
        analysis['h3_count'] = len(soup.find_all('h3'))
        
        if analysis['h1_count'] == 0:
            analysis['issues'].append('Missing H1 tag')
        elif analysis['h1_count'] > 1:
            analysis['issues'].append(f'Multiple H1 tags ({analysis["h1_count"]})')
            
        # Images
        images = soup.find_all('img')
        analysis['total_images'] = len(images)
        analysis['img_without_alt'] = len([img for img in images if not img.get('alt')])
        
        if analysis['img_without_alt'] > 0:
            analysis['issues'].append(f'{analysis["img_without_alt"]} images without alt text')
            
        # Links
        analysis['total_links'] = len(soup.find_all('a', href=True))
        
        # Word count (approximate)
        text_content = soup.get_text()
        analysis['word_count'] = len(text_content.split())
        
        # Schema markup
        analysis['has_schema_markup'] = bool(soup.find(attrs={'itemtype': True}) or 
                                           soup.find('script', {'type': 'application/ld+json'}))
        
        return analysis

    async def test_resource(self, session: aiohttp.ClientSession, url: str, resource_type: str) -> Tuple[int, float]:
        """Test if a resource (image, link) is accessible."""
        start_time = time.time()
        try:
            async with session.head(url, timeout=aiohttp.ClientTimeout(total=10)) as response:
                load_time = time.time() - start_time
                return response.status, load_time
        except:
            load_time = time.time() - start_time
            return 500, load_time

    async def crawl_site(self) -> Dict:
        """Main crawling function."""
        logger.info(f"Starting crawl of {self.base_url}")
        
        async with aiohttp.ClientSession() as session:
            while self.to_crawl and (not self.max_pages or len(self.crawled_urls) < self.max_pages):
                url = self.to_crawl.pop()
                
                if url in self.crawled_urls:
                    continue
                    
                logger.info(f"Crawling: {url} ({len(self.crawled_urls) + 1})")
                
                # Fetch page
                content, status_code, final_url, load_time = await self.fetch_page(session, url)
                self.crawled_urls.add(url)
                self.page_timings[url] = load_time
                
                # Analyze page
                if status_code == 200 and content:
                    analysis = self.analyze_page_content(content, url)
                    internal_links, external_links, images = self.extract_links(content, url)
                    
                    # Add new internal links to crawl queue
                    for link in internal_links:
                        if link not in self.crawled_urls:
                            self.to_crawl.add(link)
                    
                    # Store results
                    self.results[url] = {
                        'status_code': status_code,
                        'load_time': load_time,
                        'final_url': final_url,
                        'analysis': analysis,
                        'internal_links': internal_links,
                        'external_links': external_links,
                        'images': images
                    }
                    
                    # Test some external links (sample to avoid overwhelming)
                    for ext_link in external_links[:5]:  # Test first 5 external links
                        status, timing = await self.test_resource(session, ext_link, 'external_link')
                        self.external_links.append((url, ext_link, status))
                        if status >= 400:
                            self.broken_links.append((url, ext_link, status))
                    
                    # Test images
                    for img_url in images:
                        status, timing = await self.test_resource(session, img_url, 'image')
                        self.images.append((url, img_url, status))
                        if status >= 400:
                            self.broken_links.append((url, img_url, status))
                
                else:
                    # Failed to load page
                    self.results[url] = {
                        'status_code': status_code,
                        'load_time': load_time,
                        'final_url': final_url,
                        'analysis': {'issues': [f'Failed to load page (status {status_code})']},
                        'internal_links': [],
                        'external_links': [],
                        'images': []
                    }
                
                # Rate limiting
                if self.delay > 0:
                    await asyncio.sleep(self.delay)
        
        return self.generate_report()

    def generate_report(self) -> Dict:
        """Generate comprehensive crawl report."""
        total_time = time.time() - self.total_start_time
        
        # Calculate statistics
        successful_pages = sum(1 for r in self.results.values() if r['status_code'] == 200)
        total_pages = len(self.results)
        avg_load_time = sum(self.page_timings.values()) / len(self.page_timings) if self.page_timings else 0
        
        # SEO analysis
        pages_without_title = sum(1 for r in self.results.values() 
                                if r.get('analysis', {}).get('title') is None)
        pages_without_meta = sum(1 for r in self.results.values() 
                               if r.get('analysis', {}).get('meta_description') is None)
        
        # Performance analysis
        slow_pages = [(url, data['load_time']) for url, data in self.results.items() 
                     if data['load_time'] > 3.0]
        
        # Issues summary
        all_issues = []
        for url, data in self.results.items():
            issues = data.get('analysis', {}).get('issues', [])
            for issue in issues:
                all_issues.append((url, issue))
        
        report = {
            'summary': {
                'total_pages_crawled': total_pages,
                'successful_pages': successful_pages,
                'failed_pages': total_pages - successful_pages,
                'success_rate': (successful_pages / total_pages * 100) if total_pages > 0 else 0,
                'total_crawl_time': total_time,
                'average_page_load_time': avg_load_time,
                'total_broken_links': len(self.broken_links),
                'base_url': self.base_url
            },
            'performance': {
                'slow_pages': slow_pages,
                'fastest_page': min(self.page_timings.items(), key=lambda x: x[1]) if self.page_timings else None,
                'slowest_page': max(self.page_timings.items(), key=lambda x: x[1]) if self.page_timings else None,
                'page_timings': dict(sorted(self.page_timings.items(), key=lambda x: x[1], reverse=True))
            },
            'seo': {
                'pages_without_title': pages_without_title,
                'pages_without_meta_description': pages_without_meta,
                'title_issues': pages_without_title > 0,
                'meta_description_issues': pages_without_meta > 0
            },
            'issues': {
                'broken_links': self.broken_links,
                'all_issues': all_issues,
                'pages_with_issues': len([url for url, data in self.results.items() 
                                        if data.get('analysis', {}).get('issues')])
            },
            'detailed_results': self.results
        }
        
        return report

    def save_report(self, report: Dict, output_file: str):
        """Save report to JSON file."""
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        logger.info(f"Report saved to {output_file}")

    def print_summary(self, report: Dict):
        """Print summary to console."""
        summary = report['summary']
        performance = report['performance']
        issues = report['issues']
        
        print("\n" + "="*50)
        print("SITE CRAWL SUMMARY")
        print("="*50)
        print(f"Base URL: {summary['base_url']}")
        print(f"Total Pages: {summary['total_pages_crawled']}")
        print(f"Successful: {summary['successful_pages']}")
        print(f"Failed: {summary['failed_pages']}")
        print(f"Success Rate: {summary['success_rate']:.1f}%")
        print(f"Total Crawl Time: {summary['total_crawl_time']:.2f}s")
        print(f"Average Load Time: {summary['average_page_load_time']:.2f}s")
        
        print("\n" + "-"*30)
        print("PERFORMANCE")
        print("-"*30)
        if performance['fastest_page']:
            print(f"Fastest Page: {performance['fastest_page'][0]} ({performance['fastest_page'][1]:.2f}s)")
        if performance['slowest_page']:
            print(f"Slowest Page: {performance['slowest_page'][0]} ({performance['slowest_page'][1]:.2f}s)")
        if performance['slow_pages']:
            print(f"Slow Pages (>3s): {len(performance['slow_pages'])}")
        
        print("\n" + "-"*30)
        print("ISSUES")
        print("-"*30)
        print(f"Broken Links: {len(issues['broken_links'])}")
        print(f"Pages with Issues: {issues['pages_with_issues']}")
        print(f"Total Issues: {len(issues['all_issues'])}")
        
        if issues['broken_links']:
            print("\nBroken Links:")
            for source, link, status in issues['broken_links'][:10]:  # Show first 10
                print(f"  {status}: {link} (found on {source})")
                
        if issues['all_issues']:
            print("\nTop Issues:")
            issue_counts = defaultdict(int)
            for _, issue in issues['all_issues']:
                issue_counts[issue] += 1
            
            for issue, count in sorted(issue_counts.items(), key=lambda x: x[1], reverse=True)[:5]:
                print(f"  {issue}: {count} pages")
        
        print("\n" + "="*50)

async def main():
    parser = argparse.ArgumentParser(description="Crawl and test MkDocs site")
    parser.add_argument("url", help="Base URL to crawl (e.g., http://localhost:8000)")
    parser.add_argument("--max-pages", type=int, help="Maximum pages to crawl")
    parser.add_argument("--delay", type=float, default=0.5, help="Delay between requests (seconds)")
    parser.add_argument("--output", default="crawl_report.json", help="Output file for report")
    parser.add_argument("--quiet", action="store_true", help="Suppress console output")
    
    args = parser.parse_args()
    
    if args.quiet:
        logging.getLogger().setLevel(logging.WARNING)
    
    crawler = SiteCrawler(args.url, args.max_pages, args.delay)
    
    try:
        report = await crawler.crawl_site()
        
        # Save report
        crawler.save_report(report, args.output)
        
        # Print summary
        if not args.quiet:
            crawler.print_summary(report)
        
        # Return appropriate exit code
        if report['summary']['failed_pages'] > 0 or len(report['issues']['broken_links']) > 0:
            sys.exit(1)
        else:
            sys.exit(0)
            
    except KeyboardInterrupt:
        logger.info("Crawl interrupted by user")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Crawl failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())
