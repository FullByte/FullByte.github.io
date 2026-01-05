#!/usr/bin/env python3
"""
0xFAB1 Site Manager - Unified MkDocs site management tool

Features:
- Build site with automatic image optimization (JPG/JPEG/PNG → WebP)
- Development server with live reload
- Site statistics and analytics
- Media path validation and testing
- SVG files preserved (no conversion)

Usage: python site_manager.py <command> [options]
"""

import argparse
import subprocess
import sys
import os
import json
import re
import logging
import io
from pathlib import Path
from collections import Counter
from datetime import datetime
from urllib.parse import urljoin
from typing import List, Dict, Union, Optional

# Image processing
try:
    from PIL import Image, ImageFile
    ImageFile.LOAD_TRUNCATED_IMAGES = True
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False

# Logging setup
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

class ImageOptimizer:
    """Optimizes JPG/JPEG/PNG images to WebP format, preserves SVG files."""
    
    def __init__(self, docs_path: Path, quality: int = 85, lossless: bool = False, verbose: bool = True):
        self.docs_path = docs_path
        self.quality = quality
        self.lossless = lossless
        self.verbose = verbose
        self.stats = {'converted': 0, 'updated_files': 0, 'deleted_originals': 0, 'original_size': 0, 'webp_size': 0}

    def convert_to_webp(self, image_path: Path) -> bool:
        """Convert image to WebP format."""
        if not PIL_AVAILABLE:
            if self.verbose:
                print("⚠️ PIL/Pillow not available, skipping conversion")
            return False
            
        try:
            webp_path = image_path.with_suffix('.webp')
            
            # Skip if WebP exists and is newer
            if webp_path.exists() and webp_path.stat().st_mtime > image_path.stat().st_mtime:
                if self.verbose:
                    print(f"⏭ Skipping {image_path.relative_to(self.docs_path)} (WebP exists and is newer)")
                return True
                
            with Image.open(image_path) as img:
                # Convert RGBA to RGB for lossy WebP
                if img.mode in ('RGBA', 'LA') and not self.lossless:
                    background = Image.new('RGB', img.size, (255, 255, 255))
                    background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
                    img = background
                
                # Save as WebP
                img.save(webp_path, 'WebP', optimize=True, 
                        quality=self.quality if not self.lossless else 100, 
                        lossless=self.lossless)
                
            # Update stats
            original_size = image_path.stat().st_size
            webp_size = webp_path.stat().st_size
            self.stats['original_size'] += original_size
            self.stats['webp_size'] += webp_size
            self.stats['converted'] += 1
            
            if self.verbose:
                reduction = ((original_size - webp_size) / original_size) * 100
                print(f"✓ {image_path.relative_to(self.docs_path)}: {original_size//1024}KB → {webp_size//1024}KB ({reduction:.1f}% reduction)")
            return True
            
        except Exception as e:
            if self.verbose:
                print(f"✗ Failed to convert {image_path}: {e}")
            return False

    def update_markdown_references(self) -> None:
        """Update markdown files to use WebP images."""
        pattern = r'!\[([^\]]*)\]\(([^)]+\.(jpg|jpeg|png))\)'
        
        for md_file in self.docs_path.rglob('*.md'):
            try:
                content = md_file.read_text(encoding='utf-8')
                original_content = content
                
                def replace_with_webp(match):
                    alt_text, image_path = match.group(1), match.group(2)
                    webp_path = image_path.rsplit('.', 1)[0] + '.webp'
                    
                    if (md_file.parent / webp_path).exists():
                        return f'![{alt_text}]({webp_path})'
                    return match.group(0)
                
                content = re.sub(pattern, replace_with_webp, content)
                
                if content != original_content:
                    md_file.write_text(content, encoding='utf-8')
                    self.stats['updated_files'] += 1
                    if self.verbose:
                        print(f"✓ Updated references in {md_file.relative_to(self.docs_path)}")
                        
            except Exception as e:
                if self.verbose:
                    print(f"✗ Failed to update {md_file}: {e}")

    def cleanup_original_images(self, extensions: List[str]) -> None:
        """Delete original images that have WebP equivalents."""
        if self.verbose:
            print("🧹 Cleaning up original images...")
        
        for ext in extensions:
            for image_path in self.docs_path.rglob(f"*.{ext}"):
                webp_path = image_path.with_suffix('.webp')
                if webp_path.exists():
                    try:
                        image_path.unlink()
                        self.stats['deleted_originals'] += 1
                        if self.verbose:
                            print(f"🗑 Deleted {image_path.relative_to(self.docs_path)}")
                    except Exception as e:
                        if self.verbose:
                            print(f"✗ Failed to delete {image_path}: {e}")

    def get_image_count(self, extensions: List[str]) -> int:
        """Get count of images by extensions."""
        return sum(len(list(self.docs_path.rglob(f"*.{ext}"))) for ext in extensions)

    def print_summary(self) -> None:
        """Print optimization summary."""
        if any(self.stats.values()):
            print(f"\n📊 Optimization Summary:")
            print(f"   Images converted: {self.stats['converted']}")
            print(f"   Markdown files updated: {self.stats['updated_files']}")
            print(f"   Original images deleted: {self.stats['deleted_originals']}")
            
            if self.stats['original_size'] > 0:
                reduction = ((self.stats['original_size'] - self.stats['webp_size']) / self.stats['original_size']) * 100
                print(f"   Size reduction: {self.stats['original_size']//1024//1024}MB → {self.stats['webp_size']//1024//1024}MB ({reduction:.1f}%)")

    def optimize_for_build(self) -> bool:
        """Run optimization suitable for automated builds."""
        if not self.docs_path.exists():
            if self.verbose:
                print(f"⚠️ {self.docs_path} does not exist")
            return False
        
        extensions = ["jpg", "jpeg", "png"]
        image_count = self.get_image_count(extensions)
        
        if image_count == 0:
            if self.verbose:
                print("✅ No new images to optimize")
            return False
        
        if self.verbose:
            print("🔄 Converting new images to WebP...")
        
        has_changes = False
        for ext in extensions:
            for image_path in self.docs_path.rglob(f"*.{ext}"):
                if self.convert_to_webp(image_path):
                    has_changes = True
        
        if has_changes:
            if self.verbose:
                print("📝 Updating markdown references...")
            self.update_markdown_references()
            
            if self.verbose:
                print("🧹 Cleaning up original images...")
            self.cleanup_original_images(extensions)
            
            if self.verbose:
                self.print_summary()
        
        return has_changes


class SiteManager:
    """Main site management class."""
    
    def __init__(self):
        self.project_root = Path.cwd()
        self.docs_dir = self.project_root / "docs"
        self.site_dir = self.project_root / "site"
        
        if not (self.project_root / "mkdocs.yml").exists():
            raise ValueError("mkdocs.yml not found. Please run from project root.")

    def _run_command(self, cmd: str, description: str, quiet: bool = False) -> bool:
        """Run a command with error handling."""
        if not quiet:
            print(f"🔄 {description}...")
        
        try:
            env = os.environ.copy()
            if quiet:
                env.update({'PYTHONWARNINGS': 'ignore', 'MKDOCS_QUIET': '1'})
            
            result = subprocess.run(cmd, shell=True, check=True, text=True, env=env)
            if not quiet:
                print(f"✅ {description} completed")
            return True
        except subprocess.CalledProcessError as e:
            if not quiet:
                print(f"❌ {description} failed: {e}")
            return False

    def build_site(self, clean: bool = False, no_optimize: bool = False, quiet: bool = False) -> bool:
        """Build the MkDocs site with optional optimization."""
        print("🏗️ Building MkDocs site...")
        
        if clean and not self._run_command("mkdocs build --clean", "Cleaning previous build", quiet):
            return False
        
        # Image optimization
        if not no_optimize:
            optimizer = ImageOptimizer(self.docs_dir, quality=85, lossless=False, verbose=not quiet)
            if optimizer.optimize_for_build():
                if not quiet:
                    print("✅ Image optimization completed")
            elif not quiet:
                print("⚠️ Image optimization completed (no changes needed)")
        
        # Generate statistics
        try:
            stats_generator = SiteStatsGenerator(str(self.docs_dir))
            stats_generator.generate_all_stats()
            if not quiet:
                print("✅ Statistics generated")
        except Exception:
            if not quiet:
                print("⚠️ Statistics generation failed, continuing...")
        
        # Build site
        if not self._run_command("mkdocs build", "Building site", quiet):
            return False
        
        print("✅ Build completed successfully!")
        return True

    def serve_site(self, host: str = "127.0.0.1", port: str = "8000", clean: bool = False) -> bool:
        """Start the MkDocs development server."""
        print(f"🚀 Starting development server at http://{host}:{port}")
        print("💡 Press Ctrl+C to stop")
        print("-" * 50)
        
        cmd = f"mkdocs serve --dev-addr={host}:{port}"
        if clean:
            cmd += " --clean"
        
        try:
            subprocess.run(cmd, shell=True, check=True)
        except KeyboardInterrupt:
            print("\n👋 Server stopped")
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to start server: {e}")
            return False
        return True

    def optimize_images(self, mode: str = "all", quality: int = 85, lossless: bool = False, quiet: bool = False) -> bool:
        """Run image optimization."""
        try:
            optimizer = ImageOptimizer(self.docs_dir, quality=quality, lossless=lossless, verbose=not quiet)
            
            if mode == "build":
                return optimizer.optimize_for_build()
            
            extensions = ["jpg", "jpeg", "png"]
            image_count = optimizer.get_image_count(extensions)
            
            if image_count == 0:
                if not quiet:
                    print("✅ No images to optimize")
                return True
            
            if not quiet:
                print("🔄 Converting images to WebP...")
            
            has_changes = False
            for ext in extensions:
                for image_path in self.docs_dir.rglob(f"*.{ext}"):
                    if optimizer.convert_to_webp(image_path):
                        has_changes = True
            
            if has_changes and mode in ["update", "all"]:
                if not quiet:
                    print("📝 Updating markdown references...")
                optimizer.update_markdown_references()
            
            if has_changes and mode in ["cleanup", "all"]:
                if not quiet:
                    print("🧹 Cleaning up original images...")
                optimizer.cleanup_original_images(extensions)
            
            if not quiet:
                optimizer.print_summary()
            return True
            
        except Exception as e:
            if not quiet:
                print(f"❌ Image optimization failed: {e}")
            return False

    def generate_stats(self, quiet: bool = False) -> bool:
        """Generate site statistics (always exports JSON)."""
        try:
            stats_generator = SiteStatsGenerator(str(self.docs_dir))
            stats_generator.generate_all_stats()
            output_file = stats_generator.last_json
            if output_file:
                print(f"📊 Statistics exported to {output_file}")
            if not quiet:
                print("📊 Site statistics generated successfully!")
            return True
        except Exception as e:
            if not quiet:
                print(f"❌ Statistics generation failed: {e}")
            return False

    def test_site(self, output_format: str = "console") -> bool:
        """Test the built site for issues."""
        if not self.site_dir.exists():
            print("❌ Site directory not found. Please build the site first.")
            return False
        
        try:
            tester = SimpleSiteTester(str(self.site_dir))
            results = tester.run_all_tests()
            
            if output_format == "json":
                output_file = self.project_root / "test_results.json"
                with open(output_file, 'w', encoding='utf-8') as f:
                    json.dump(results, f, indent=2, default=str)
                print(f"🧪 Test results exported to {output_file}")
            else:
                self._print_test_results(results)
            return True
        except Exception as e:
            print(f"❌ Site testing failed: {e}")
            return False

    def _print_test_results(self, results: Dict) -> None:
        """Print test results."""
        print(f"\n🧪 Site Test Results")
        print("=" * 50)
        print(f"Total HTML files: {results.get('total_files', 0)}")
        print(f"Total issues found: {len(results.get('issues', []))}")
        
        if results.get('issues'):
            print("\n⚠️ Issues found:")
            for issue in results['issues'][:10]:
                print(f"  • {issue}")
            if len(results['issues']) > 10:
                print(f"  ... and {len(results['issues']) - 10} more issues")
        else:
            print("✅ No issues found!")

    def check_media_paths(self) -> bool:
        """Check media file paths and references."""
        print("🔍 Checking media paths...")
        try:
            checker = MediaPathChecker(str(self.docs_dir))
            issues = checker.check_all_media()
            
            if issues:
                print(f"⚠️ Found {len(issues)} media path issues:")
                for issue in issues[:10]:
                    print(f"  • {issue}")
                if len(issues) > 10:
                    print(f"  ... and {len(issues) - 10} more issues")
            else:
                print("✅ No media path issues found!")
            return True
        except Exception as e:
            print(f"❌ Media path check failed: {e}")
            return False

    def clean_build(self) -> bool:
        """Clean build artifacts."""
        print("🧹 Cleaning build artifacts...")
        artifacts = [
            self.site_dir,
            self.project_root / ".cache",
            self.project_root / "__pycache__"
        ]
        
        cleaned = 0
        for artifact in artifacts:
            if artifact.exists():
                if artifact.is_dir():
                    import shutil
                    shutil.rmtree(artifact)
                else:
                    artifact.unlink()
                cleaned += 1
        
        print(f"✅ Cleaned {cleaned} artifacts")
        return True


class SiteStatsGenerator:
    """Generate comprehensive site statistics."""
    
    def __init__(self, docs_dir):
        self.docs_dir = Path(docs_dir)
        self.stats_file = self.docs_dir / "about" / "website" / "stats.md"
        self.stats_dir = self.stats_file.parent
        self.last_json = None
    
    def build_stats(self):
        """Collect stats without writing outputs."""
        return {
            'generated_at': datetime.now().isoformat(),
            'content_stats': self.analyze_content(),
            'file_stats': self.analyze_files(),
            'image_stats': self.analyze_images()
        }
    
    def generate_all_stats(self):
        """Generate all site statistics, export JSON, and write markdown."""
        stats = self.build_stats()
        json_path = self.write_json_export(stats)
        self.last_json = json_path
        self.write_stats_file(stats)
        return stats
    
    def analyze_content(self):
        """Analyze content statistics."""
        md_files = list(self.docs_dir.rglob("*.md"))
        total_words = 0
        total_lines = 0
        
        for file_path in md_files:
            try:
                content = file_path.read_text(encoding='utf-8')
                total_words += len(content.split())
                total_lines += len(content.splitlines())
            except Exception:
                continue
        
        return {
            'markdown_files': len(md_files),
            'total_words': total_words,
            'total_lines': total_lines,
            'avg_words_per_file': total_words // len(md_files) if md_files else 0
        }
    
    def analyze_files(self):
        """Analyze file statistics."""
        all_files = list(self.docs_dir.rglob("*"))
        file_types = Counter(f.suffix.lower() for f in all_files if f.is_file())
        
        return {
            'total_files': len([f for f in all_files if f.is_file()]),
            'file_types': dict(file_types),
            'directories': len([f for f in all_files if f.is_dir()])
        }
    
    def analyze_images(self):
        """Analyze image statistics."""
        image_exts = {'.webp', '.jpg', '.jpeg', '.png', '.gif', '.svg'}
        images = [f for f in self.docs_dir.rglob("*") if f.suffix.lower() in image_exts]
        
        total_size = sum(f.stat().st_size for f in images if f.exists())
        
        return {
            'total_images': len(images),
            'total_size_mb': round(total_size / (1024 * 1024), 2),
            'by_type': dict(Counter(f.suffix.lower() for f in images))
        }
    
    def write_json_export(self, stats):
        """Write stats JSON with dated filename in the stats directory."""
        if not self.stats_dir.exists():
            self.stats_dir.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.now().strftime("%Y-%m-%d-%H%M%S")
        output_file = self.stats_dir / f"_site_stats-{timestamp}.json"
        output_file.write_text(json.dumps(stats, indent=2, default=str), encoding="utf-8")
        return output_file
    
    def format_history_table(self):
        """Build a markdown table linking available JSON stats exports."""
        files = sorted(self.stats_dir.glob("_site_stats-*.json"), key=lambda p: p.name, reverse=True)

        if not files:
            return "_No JSON history available yet._"

        rows = ["| Date | JSON |", "| --- | --- |"]
        for path in files:
            rows.append(f"| {self._pretty_date_from_filename(path)} | [{path.name}]({path.name}) |")
        return "\n".join(rows)
    
    def _pretty_date_from_filename(self, path: Path) -> str:
        """Extract a readable timestamp from a stats filename."""
        match = re.match(r"_site_stats-(\d{4}-\d{2}-\d{2})(?:-(\d{6}))?", path.name)
        if match:
            date_part = match.group(1)
            time_part = match.group(2)
            if time_part:
                return f"{date_part} {time_part[:2]}:{time_part[2:4]}:{time_part[4:]}"
            return date_part
        return datetime.fromtimestamp(path.stat().st_mtime).isoformat(timespec="seconds")
    
    def write_stats_file(self, stats):
        """Write statistics to markdown file."""
        if not self.stats_dir.exists():
            self.stats_dir.mkdir(parents=True, exist_ok=True)
        history_table = self.format_history_table()
        
        content = f"""# Site Statistics

*Generated on {stats['generated_at']}*

## Content Overview

- **Markdown Files**: {stats['content_stats']['markdown_files']}
- **Total Words**: {stats['content_stats']['total_words']:,}
- **Total Lines**: {stats['content_stats']['total_lines']:,}
- **Average Words per File**: {stats['content_stats']['avg_words_per_file']}

## File Statistics

- **Total Files**: {stats['file_stats']['total_files']}
- **Directories**: {stats['file_stats']['directories']}

### File Types
{self.format_file_types(stats['file_stats']['file_types'])}

## Image Statistics

- **Total Images**: {stats['image_stats']['total_images']}
- **Total Size**: {stats['image_stats']['total_size_mb']} MB

### Image Types
{self.format_image_types(stats['image_stats']['by_type'])}

## JSON History

{history_table}
"""
        
        self.stats_file.write_text(content, encoding='utf-8')
    
    def format_file_types(self, file_types):
        """Format file types for markdown."""
        lines = []
        for ext, count in sorted(file_types.items(), key=lambda x: x[1], reverse=True)[:10]:
            ext_name = ext if ext else 'no extension'
            lines.append(f"- **{ext_name}**: {count}")
        return '\n'.join(lines)
    
    def format_image_types(self, image_types):
        """Format image types for markdown."""
        lines = []
        for ext, count in sorted(image_types.items(), key=lambda x: x[1], reverse=True):
            lines.append(f"- **{ext}**: {count}")
        return '\n'.join(lines)


class SimpleSiteTester:
    """Simple site testing functionality."""
    
    def __init__(self, site_dir):
        self.site_dir = Path(site_dir)
        self.issues = []
    
    def run_all_tests(self):
        """Run all site tests."""
        html_files = list(self.site_dir.rglob("*.html"))
        
        for html_file in html_files:
            self.test_html_file(html_file)
        
        return {
            'total_files': len(html_files),
            'issues': self.issues
        }
    
    def test_html_file(self, html_file):
        """Test a single HTML file."""
        try:
            content = html_file.read_text(encoding='utf-8')
            
            # Check for basic HTML structure
            if '<html' not in content.lower():
                self.issues.append(f"{html_file.name}: Missing <html> tag")
            
            if '<title>' not in content.lower():
                self.issues.append(f"{html_file.name}: Missing <title> tag")
            
            # Check for broken internal links
            link_pattern = r'href="([^"]+)"'
            for match in re.finditer(link_pattern, content):
                link = match.group(1)
                if link.startswith('/') or link.startswith('./'):
                    # Internal link - check if file exists
                    link_path = self.site_dir / link.lstrip('./')
                    if not link_path.exists() and not (link_path.parent / 'index.html').exists():
                        self.issues.append(f"{html_file.name}: Broken internal link: {link}")
        
        except Exception as e:
            self.issues.append(f"{html_file.name}: Error reading file: {e}")


class MediaPathChecker:
    """Check media file paths and references."""
    
    def __init__(self, docs_dir):
        self.docs_dir = Path(docs_dir)
    
    def check_all_media(self):
        """Check all media references."""
        issues = []
        md_files = list(self.docs_dir.rglob("*.md"))
        
        patterns = [
            (r'!\[[^\]]*\]\(([^)]+)\)', "markdown image"),
            (r'<img[^>]*src="([^"]+)"', "HTML image"),
            (r'<source\s+src="([^"]+)"', "audio/video source")
        ]
        
        for md_file in md_files:
            try:
                content = md_file.read_text(encoding='utf-8')
                relative_path = md_file.relative_to(self.docs_dir)
                
                for pattern, media_type in patterns:
                    for match in re.finditer(pattern, content):
                        media_path = match.group(1)
                        
                        # Skip external URLs
                        if media_path.startswith(('http://', 'https://')):
                            continue
                        
                        # Check if file exists
                        if media_path.startswith('/'):
                            full_path = self.docs_dir / media_path.lstrip('/')
                        else:
                            full_path = md_file.parent / media_path
                        
                        if not full_path.exists():
                            issues.append(f"{relative_path}: Missing {media_type}: {media_path}")
            
            except Exception as e:
                issues.append(f"{md_file.name}: Error reading file: {e}")
        
        return issues


def main():
    """Main entry point with command parsing."""
    parser = argparse.ArgumentParser(description="0xFAB1 Site Manager")
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Build command
    build_parser = subparsers.add_parser('build', help='Build the site')
    build_parser.add_argument('--clean', action='store_true', help='Clean build')
    build_parser.add_argument('--no-optimize', action='store_true', help='Skip image optimization')
    build_parser.add_argument('--quiet', action='store_true', help='Quiet output')
    
    # Serve command
    serve_parser = subparsers.add_parser('serve', help='Start development server')
    serve_parser.add_argument('--host', default='127.0.0.1', help='Host address')
    serve_parser.add_argument('--port', default='8000', help='Port number')
    serve_parser.add_argument('--clean', action='store_true', help='Clean serve')
    
    # Optimize command
    opt_parser = subparsers.add_parser('optimize', help='Optimize images')
    opt_parser.add_argument('--mode', default='all', choices=['convert', 'update', 'cleanup', 'all'])
    opt_parser.add_argument('--quality', type=int, default=85, help='WebP quality (1-100)')
    opt_parser.add_argument('--lossless', action='store_true', help='Use lossless compression')
    opt_parser.add_argument('--quiet', action='store_true', help='Quiet output')
    
    # Stats command
    subparsers.add_parser('stats', help='Generate statistics')
    
    # Test command
    test_parser = subparsers.add_parser('test', help='Test the site')
    test_parser.add_argument('--format', default='console', choices=['console', 'json'])
    
    # Check command
    subparsers.add_parser('check', help='Check media paths')
    
    # Clean command
    subparsers.add_parser('clean', help='Clean build artifacts')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    try:
        manager = SiteManager()
        
        if args.command == 'build':
            success = manager.build_site(
                clean=args.clean,
                no_optimize=args.no_optimize,
                quiet=args.quiet
            )
        elif args.command == 'serve':
            success = manager.serve_site(
                host=args.host,
                port=args.port,
                clean=args.clean
            )
        elif args.command == 'optimize':
            success = manager.optimize_images(
                mode=args.mode,
                quality=args.quality,
                lossless=args.lossless,
                quiet=args.quiet
            )
        elif args.command == 'stats':
            success = manager.generate_stats()
        elif args.command == 'test':
            success = manager.test_site(output_format=args.format)
        elif args.command == 'check':
            success = manager.check_media_paths()
        elif args.command == 'clean':
            success = manager.clean_build()
        else:
            print(f"Unknown command: {args.command}")
            success = False
        
        sys.exit(0 if success else 1)
    
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
