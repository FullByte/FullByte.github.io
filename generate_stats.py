#!/usr/bin/env python3
"""
Site Statistics Generator for MkDocs
Analyzes the site content and updates stats.md with comprehensive metrics
"""

import os
import re
import json
import time
from pathlib import Path
from collections import defaultdict, Counter
from datetime import datetime
import hashlib
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class SiteStatsGenerator:
    def __init__(self, docs_dir: str = "docs", stats_file: str = None):
        self.docs_dir = Path(docs_dir)
        if stats_file:
            self.stats_file = Path(stats_file)
        else:
            self.stats_file = self.docs_dir / "about" / "0xfab1" / "stats.md"
        
        if not self.docs_dir.exists():
            raise ValueError(f"Docs directory {docs_dir} does not exist")
        
        self.previous_stats = self.load_previous_stats()
        self.current_stats = {}
        
    def load_previous_stats(self):
        """Load previous statistics from a cache file."""
        cache_file = self.docs_dir.parent / ".stats_cache.json"
        if cache_file.exists():
            try:
                with open(cache_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                logger.warning(f"Could not load previous stats: {e}")
        return {}
    
    def save_stats_cache(self, stats):
        """Save current statistics to cache file."""
        cache_file = self.docs_dir.parent / ".stats_cache.json"
        try:
            with open(cache_file, 'w', encoding='utf-8') as f:
                json.dump(stats, f, indent=2, ensure_ascii=False)
        except Exception as e:
            logger.warning(f"Could not save stats cache: {e}")
    
    def analyze_markdown_file(self, file_path: Path):
        """Analyze a single markdown file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            logger.warning(f"Could not read {file_path}: {e}")
            return None
        
        # Calculate file stats
        file_size = file_path.stat().st_size
        modification_time = file_path.stat().st_mtime
        content_hash = hashlib.md5(content.encode('utf-8')).hexdigest()
        
        # Text analysis
        words = len(re.findall(r'\b\w+\b', content))
        lines = len(content.splitlines())
        chars = len(content)
        chars_no_spaces = len(re.sub(r'\s', '', content))
        
        # Extract headings
        headings = re.findall(r'^(#{1,6})\s+(.+)$', content, re.MULTILINE)
        heading_levels = [len(h[0]) for h in headings]
        heading_texts = [h[1].strip() for h in headings]
        
        # Extract links
        markdown_links = re.findall(r'\[([^\]]*)\]\(([^)]+)\)', content)
        internal_links = [link[1] for link in markdown_links if not link[1].startswith(('http://', 'https://'))]
        external_links = [link[1] for link in markdown_links if link[1].startswith(('http://', 'https://'))]
        
        # Extract images
        images = re.findall(r'!\[([^\]]*)\]\(([^)]+)\)', content)
        image_formats = defaultdict(int)
        for _, img_path in images:
            ext = Path(img_path).suffix.lower()
            if ext:
                image_formats[ext] += 1
        
        # Extract code blocks
        code_blocks = re.findall(r'```(\w+)?\n(.*?)```', content, re.DOTALL)
        code_languages = [block[0] for block in code_blocks if block[0]]
        
        # Calculate reading time (average 200 words per minute)
        reading_time_minutes = max(1, round(words / 200))
        
        return {
            'file_path': str(file_path.relative_to(self.docs_dir)),
            'file_size_bytes': file_size,
            'modification_time': modification_time,
            'content_hash': content_hash,
            'words': words,
            'lines': lines,
            'characters': chars,
            'characters_no_spaces': chars_no_spaces,
            'reading_time_minutes': reading_time_minutes,
            'headings': {
                'total': len(headings),
                'by_level': dict(Counter(heading_levels)),
                'texts': heading_texts
            },
            'links': {
                'total': len(markdown_links),
                'internal': len(internal_links),
                'external': len(external_links),
                'external_domains': list(set([self.extract_domain(link) for link in external_links]))
            },
            'images': {
                'total': len(images),
                'formats': dict(image_formats)
            },
            'code': {
                'blocks': len(code_blocks),
                'languages': list(set(code_languages))
            }
        }
    
    def extract_domain(self, url):
        """Extract domain from URL."""
        try:
            from urllib.parse import urlparse
            return urlparse(url).netloc
        except:
            return url.split('/')[2] if url.count('/') >= 2 else url
    
    def analyze_site(self):
        """Analyze the entire site."""
        logger.info("Starting site analysis...")
        
        # Find all markdown files
        md_files = list(self.docs_dir.rglob("*.md"))
        logger.info(f"Found {len(md_files)} markdown files")
        
        # Analyze each file
        file_analyses = []
        for md_file in md_files:
            analysis = self.analyze_markdown_file(md_file)
            if analysis:
                file_analyses.append(analysis)
        
        # Calculate aggregate statistics
        total_words = sum(f['words'] for f in file_analyses)
        total_chars = sum(f['characters'] for f in file_analyses)
        total_size_bytes = sum(f['file_size_bytes'] for f in file_analyses)
        total_reading_time = sum(f['reading_time_minutes'] for f in file_analyses)
        
        # Aggregate by directory/topic
        topics = defaultdict(lambda: {
            'files': 0, 'words': 0, 'size_bytes': 0, 'reading_time': 0
        })
        
        for analysis in file_analyses:
            file_path = Path(analysis['file_path'])
            topic = str(file_path.parent) if file_path.parent != Path('.') else 'root'
            topics[topic]['files'] += 1
            topics[topic]['words'] += analysis['words']
            topics[topic]['size_bytes'] += analysis['file_size_bytes']
            topics[topic]['reading_time'] += analysis['reading_time_minutes']
        
        # Most recent modifications
        recent_files = sorted(file_analyses, key=lambda x: x['modification_time'], reverse=True)[:10]
        
        # Largest files
        largest_files = sorted(file_analyses, key=lambda x: x['words'], reverse=True)[:10]
        
        # Aggregate all statistics first
        stats = {
            'generation_time': datetime.now().isoformat(),
            'total_files': len(file_analyses),
            'total_words': total_words,
            'total_characters': total_chars,
            'total_size_bytes': total_size_bytes,
            'total_size_mb': round(total_size_bytes / 1024 / 1024, 2),
            'total_reading_time_minutes': total_reading_time,
            'total_reading_time_hours': round(total_reading_time / 60, 1),
            'topics': dict(topics),
            'recent_files': [
                {
                    'path': f['file_path'],
                    'words': f['words'],
                    'modified': datetime.fromtimestamp(f['modification_time']).strftime('%Y-%m-%d %H:%M')
                }
                for f in recent_files
            ],
            'largest_files': [
                {
                    'path': f['file_path'],
                    'words': f['words'],
                    'reading_time': f['reading_time_minutes']
                }
                for f in largest_files
            ],
            'file_details': file_analyses
        }
        
        # Detect changes after setting basic stats
        changes = self.detect_changes(file_analyses, total_words, total_size_bytes)
        stats['changes'] = changes
        
        self.current_stats = stats
        return stats
    
    def detect_changes(self, current_files, total_words=0, total_size_bytes=0):
        """Detect changes since last run."""
        if not self.previous_stats:
            return {
                'new_files': len(current_files),
                'modified_files': 0,
                'deleted_files': 0,
                'word_change': total_words,
                'size_change_bytes': total_size_bytes,
                'new_file_list': [],
                'modified_file_list': [],
                'deleted_file_list': []
            }
        
        prev_files = {f['file_path']: f for f in self.previous_stats.get('file_details', [])}
        curr_files = {f['file_path']: f for f in current_files}
        
        new_files = set(curr_files.keys()) - set(prev_files.keys())
        deleted_files = set(prev_files.keys()) - set(curr_files.keys())
        
        modified_files = []
        for path in set(curr_files.keys()) & set(prev_files.keys()):
            if curr_files[path]['content_hash'] != prev_files[path]['content_hash']:
                modified_files.append(path)
        
        word_change = total_words - self.previous_stats.get('total_words', 0)
        size_change = total_size_bytes - self.previous_stats.get('total_size_bytes', 0)
        
        return {
            'new_files': len(new_files),
            'modified_files': len(modified_files),
            'deleted_files': len(deleted_files),
            'word_change': word_change,
            'size_change_bytes': size_change,
            'new_file_list': list(new_files)[:5],  # Show first 5
            'modified_file_list': modified_files[:5],  # Show first 5
            'deleted_file_list': list(deleted_files)[:5]  # Show first 5
        }
    
    def format_stats_section(self, stats):
        """Format statistics as markdown section."""
        date_str = datetime.now().strftime('%d.%m.%Y')
        time_str = datetime.now().strftime('%H:%M')
        
        section = f"""### {date_str}

**Generated:** {time_str}

#### 📊 Overview
- **Total Files:** {stats['total_files']} markdown files
- **Total Words:** {stats['total_words']:,} words
- **Total Size:** {stats['total_size_mb']} MB ({stats['total_size_bytes']:,} bytes)
- **Reading Time:** {stats['total_reading_time_hours']} hours ({stats['total_reading_time_minutes']} minutes)

#### 📈 Changes Since Last Update
- **New Files:** {stats['changes']['new_files']}
- **Modified Files:** {stats['changes']['modified_files']}
- **Deleted Files:** {stats['changes']['deleted_files']}
- **Word Count Change:** {stats['changes']['word_change']:+,}
- **Size Change:** {stats['changes']['size_change_bytes']:+,} bytes

#### 📁 Content by Topic
"""
        
        # Sort topics by word count
        sorted_topics = sorted(stats['topics'].items(), key=lambda x: x[1]['words'], reverse=True)
        for topic, data in sorted_topics:
            if data['reading_time'] < 60:
                reading_time = f"{data['reading_time']} min"
            else:
                hours = data['reading_time'] // 60
                minutes = data['reading_time'] % 60
                reading_time = f"{hours}h {minutes}m"
            section += f"- **{topic}:** {data['files']} files, {data['words']:,} words, {reading_time}\n"
        
        section += "\n#### 📝 Recently Modified Files\n"
        for file_info in stats['recent_files'][:5]:
            section += f"- `{file_info['path']}` - {file_info['words']} words (modified {file_info['modified']})\n"
        
        section += "\n#### 📚 Largest Files\n"
        for file_info in stats['largest_files'][:5]:
            section += f"- `{file_info['path']}` - {file_info['words']:,} words ({file_info['reading_time']} min read)\n"
        
        if stats['changes']['new_files'] > 0:
            section += "\n#### 🆕 New Files\n"
            for new_file in stats['changes']['new_file_list']:
                section += f"- `{new_file}`\n"
        
        if stats['changes']['modified_files'] > 0:
            section += "\n#### ✏️ Modified Files\n"
            for mod_file in stats['changes']['modified_file_list']:
                section += f"- `{mod_file}`\n"
        
        section += "\n---\n\n"
        return section
    
    def update_stats_file(self, stats):
        """Update the stats.md file with new statistics."""
        # Read current content
        if self.stats_file.exists():
            with open(self.stats_file, 'r', encoding='utf-8') as f:
                content = f.read()
        else:
            # Create basic structure if file doesn't exist
            content = """# Stats

This is an automatically created page with some insights on the content of this website.

## Current

The stats ordered by date (everytime the script runs)

"""
        
        # Find the insertion point (after "## Current" section)
        marker_text = "The stats ordered by date (everytime the script runs)"
        
        new_section = self.format_stats_section(stats)
        
        if marker_text in content:
            # Find position after the marker
            marker_pos = content.find(marker_text) + len(marker_text)
            # Find the next newline after marker
            next_newline = content.find('\n', marker_pos)
            if next_newline != -1:
                # Insert new section after the marker line
                updated_content = content[:next_newline + 1] + '\n' + new_section + content[next_newline + 1:]
            else:
                updated_content = content + '\n' + new_section
        else:
            # Fallback: append to end
            updated_content = content + '\n' + new_section
        
        # Write updated content
        with open(self.stats_file, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        logger.info(f"Updated stats file: {self.stats_file}")
    
    def run(self):
        """Run the complete statistics generation process."""
        logger.info("Starting site statistics generation...")
        
        # Analyze site
        stats = self.analyze_site()
        
        # Update stats file
        self.update_stats_file(stats)
        
        # Save cache for next run
        self.save_stats_cache(stats)
        
        logger.info("Statistics generation completed!")
        
        # Print summary
        print(f"\n📊 Site Statistics Summary")
        print(f"Total Files: {stats['total_files']}")
        print(f"Total Words: {stats['total_words']:,}")
        print(f"Total Size: {stats['total_size_mb']} MB")
        print(f"Reading Time: {stats['total_reading_time_hours']} hours")
        print(f"Changes: +{stats['changes']['new_files']} new, {stats['changes']['modified_files']} modified")
        print(f"Stats saved to: {self.stats_file}")
        
        return stats

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Generate site statistics")
    parser.add_argument("--docs-dir", default="docs", help="Path to docs directory")
    parser.add_argument("--stats-file", help="Path to stats.md file (default: docs/about/0xfab1/stats.md)")
    parser.add_argument("--quiet", action="store_true", help="Suppress console output")
    
    args = parser.parse_args()
    
    if args.quiet:
        logging.getLogger().setLevel(logging.WARNING)
    
    try:
        generator = SiteStatsGenerator(args.docs_dir, args.stats_file)
        stats = generator.run()
        return 0
    except Exception as e:
        logger.error(f"Statistics generation failed: {e}")
        return 1

if __name__ == "__main__":
    exit(main())
