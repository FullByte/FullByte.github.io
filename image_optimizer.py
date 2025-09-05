#!/usr/bin/env python3
"""
Comprehensive Image Optimizer for MkDocs
Converts images to WebP format, updates markdown references, and cleans up original files
"""

import os
import sys
import re
import io
from pathlib import Path
from PIL import Image, ImageFile
import argparse
from typing import List, Tuple, Dict, Union

# Handle truncated images
ImageFile.LOAD_TRUNCATED_IMAGES = True

class ImageOptimizer:
    def __init__(self, docs_path: Path, quality: int = 85, lossless: bool = False, verbose: bool = True):
        self.docs_path = docs_path
        self.quality = quality
        self.lossless = lossless
        self.verbose = verbose
        self.stats = {
            'converted': 0,
            'updated_files': 0,
            'deleted_originals': 0,
            'original_size': 0,
            'webp_size': 0
        }

    def convert_to_webp(self, image_path: Path) -> bool:
        """Convert an image to WebP format."""
        try:
            webp_path = image_path.with_suffix('.webp')
            
            # Skip if WebP already exists and is newer
            if webp_path.exists() and webp_path.stat().st_mtime > image_path.stat().st_mtime:
                if self.verbose:
                    print(f"⏭ Skipping {image_path.relative_to(self.docs_path)} (WebP exists and is newer)")
                return True
                
            with Image.open(image_path) as img:
                # Convert RGBA to RGB if saving as lossy WebP
                if img.mode in ('RGBA', 'LA') and not self.lossless:
                    background = Image.new('RGB', img.size, (255, 255, 255))
                    background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
                    img = background
                
                # Save as WebP
                save_kwargs = {
                    'format': 'WebP',
                    'optimize': True,
                    'quality': self.quality if not self.lossless else 100,
                    'lossless': self.lossless
                }
                
                img.save(webp_path, **save_kwargs)
                
            original_size = image_path.stat().st_size
            webp_size = webp_path.stat().st_size
            reduction = ((original_size - webp_size) / original_size) * 100
            
            self.stats['original_size'] += original_size
            self.stats['webp_size'] += webp_size
            self.stats['converted'] += 1
            
            if self.verbose:
                print(f"✓ {image_path.relative_to(self.docs_path)}: {original_size//1024}KB → {webp_size//1024}KB ({reduction:.1f}% reduction)")
            return True
            
        except Exception as e:
            if self.verbose:
                print(f"✗ Failed to convert {image_path}: {e}")
            return False

    def update_markdown_references(self, use_clean_references: bool = False) -> None:
        """Update markdown files to use WebP images."""
        markdown_files = list(self.docs_path.rglob('*.md'))
        
        for md_file in markdown_files:
            try:
                content = md_file.read_text(encoding='utf-8')
                original_content = content
                
                if use_clean_references:
                    # Clean format: ![alt](image.webp)
                    # Replace picture elements with simple img references
                    picture_pattern = r'<picture><source srcset="([^"]+\.webp)" type="image/webp"><img src="[^"]+" alt="([^"]*)"></picture>'
                    content = re.sub(picture_pattern, r'![\2](\1)', content)
                    
                    # Replace direct image references with WebP equivalents
                    img_pattern = r'!\[([^\]]*)\]\(([^)]+\.(jpg|jpeg|png))\)'
                    
                    def replace_with_webp(match):
                        alt_text = match.group(1)
                        image_path = match.group(2)
                        webp_path = image_path.rsplit('.', 1)[0] + '.webp'
                        
                        # Check if WebP file exists
                        full_webp_path = md_file.parent / webp_path
                        if full_webp_path.exists():
                            return f'![{alt_text}]({webp_path})'
                        else:
                            return match.group(0)  # Keep original if WebP doesn't exist
                    
                    content = re.sub(img_pattern, replace_with_webp, content)
                    
                else:
                    # Fallback format: <picture> elements with WebP and fallback
                    img_pattern = r'!\[([^\]]*)\]\(([^)]+\.(jpg|jpeg|png))\)'
                    
                    def replace_with_picture(match):
                        alt_text = match.group(1)
                        image_path = match.group(2)
                        webp_path = image_path.rsplit('.', 1)[0] + '.webp'
                        
                        # Check if WebP file exists
                        full_webp_path = md_file.parent / webp_path
                        if full_webp_path.exists():
                            return f'<picture><source srcset="{webp_path}" type="image/webp"><img src="{image_path}" alt="{alt_text}"></picture>'
                        else:
                            return match.group(0)  # Keep original if WebP doesn't exist
                    
                    content = re.sub(img_pattern, replace_with_picture, content)
                
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
            print("\n🧹 Cleaning up original images...")
        
        for ext in extensions:
            pattern = f"*.{ext}"
            images = list(self.docs_path.rglob(pattern))
            
            for image_path in images:
                webp_path = image_path.with_suffix('.webp')
                
                # Only delete if WebP exists
                if webp_path.exists():
                    try:
                        image_path.unlink()
                        self.stats['deleted_originals'] += 1
                        if self.verbose:
                            print(f"🗑 Deleted {image_path.relative_to(self.docs_path)}")
                    except Exception as e:
                        if self.verbose:
                            print(f"✗ Failed to delete {image_path}: {e}")

    def get_image_inventory(self, extensions: List[str]) -> Dict[str, int]:
        """Get inventory of images by type."""
        inventory = {}
        
        # Count WebP images
        webp_images = list(self.docs_path.rglob('*.webp'))
        inventory['webp'] = len(webp_images)
        
        # Count original images by extension
        for ext in extensions:
            pattern = f"*.{ext}"
            images = list(self.docs_path.rglob(pattern))
            inventory[ext] = len(images)
        
        # Count animated GIFs separately
        gif_images = list(self.docs_path.rglob('*.gif'))
        inventory['gif'] = len(gif_images)
        
        return inventory

    def print_summary(self) -> None:
        """Print optimization summary."""
        print(f"\n📊 Optimization Summary:")
        print(f"   Images converted: {self.stats['converted']}")
        print(f"   Markdown files updated: {self.stats['updated_files']}")
        print(f"   Original images deleted: {self.stats['deleted_originals']}")
        
        if self.stats['original_size'] > 0:
            total_reduction = ((self.stats['original_size'] - self.stats['webp_size']) / self.stats['original_size']) * 100
            print(f"   Size reduction: {self.stats['original_size']//1024//1024}MB → {self.stats['webp_size']//1024//1024}MB ({total_reduction:.1f}%)")

def optimize_for_build(docs_path: Union[str, Path] = "docs", quiet: bool = False) -> bool:
    """
    Optimized function for build integration.
    Runs image optimization suitable for automated builds.
    
    Returns:
        bool: True if any changes were made, False otherwise
    """
    docs_path = Path(docs_path)
    if not docs_path.exists():
        if not quiet:
            print(f"Warning: {docs_path} does not exist, skipping image optimization")
        return False
    
    optimizer = ImageOptimizer(docs_path, quality=85, lossless=False, verbose=not quiet)
    
    # Get initial state
    initial_inventory = optimizer.get_image_inventory(["jpg", "jpeg", "png", "svg"])
    has_changes = False
    
    # Convert any new images
    if initial_inventory.get('jpg', 0) + initial_inventory.get('jpeg', 0) + initial_inventory.get('png', 0) > 0:
        if not quiet:
            print("🔄 Converting new images to WebP...")
        
        for ext in ["jpg", "jpeg", "png"]:
            images = list(docs_path.rglob(f"*.{ext}"))
            for image_path in images:
                if optimizer.convert_to_webp(image_path):
                    has_changes = True
    
    # Update markdown references if changes were made
    if has_changes:
        if not quiet:
            print("📝 Updating markdown references...")
        optimizer.update_markdown_references(use_clean_references=True)
        
        if not quiet:
            print("🧹 Cleaning up original images...")
        optimizer.cleanup_original_images(["jpg", "jpeg", "png"])
    
    # Handle SVG files (convert to WebP but keep originals for compatibility)
    svg_images = list(docs_path.rglob("*.svg"))
    for svg_path in svg_images:
        webp_path = svg_path.with_suffix('.webp')
        if not webp_path.exists():
            try:
                # Try to convert SVG to WebP (requires cairosvg for better SVG support)
                try:
                    import cairosvg
                    # Convert SVG to PNG first, then to WebP
                    png_data = cairosvg.svg2png(url=str(svg_path))
                    img = Image.open(io.BytesIO(png_data))
                    img.save(webp_path, 'WebP', quality=85, optimize=True)
                    
                    if not quiet:
                        print(f"✓ Converted SVG to WebP: {svg_path.relative_to(docs_path)}")
                    has_changes = True
                except ImportError:
                    if not quiet:
                        print(f"⚠ SVG conversion skipped (cairosvg not installed): {svg_path.relative_to(docs_path)}")
                
            except Exception as e:
                if not quiet:
                    print(f"✗ Failed to convert SVG {svg_path}: {e}")
    
    if has_changes and not quiet:
        optimizer.print_summary()
    elif not quiet and initial_inventory.get('jpg', 0) + initial_inventory.get('jpeg', 0) + initial_inventory.get('png', 0) == 0:
        print("✅ No new images to optimize")
    
    return has_changes

def main():
    parser = argparse.ArgumentParser(description="Comprehensive image optimization for MkDocs")
    parser.add_argument("--docs-path", default="docs", help="Path to docs directory")
    parser.add_argument("--quality", type=int, default=85, help="WebP quality (1-100)")
    parser.add_argument("--lossless", action="store_true", help="Use lossless WebP compression")
    parser.add_argument("--extensions", nargs="+", default=["jpg", "jpeg", "png"], help="Image extensions to convert")
    parser.add_argument("--mode", choices=["convert", "update", "cleanup", "all", "build"], default="all", 
                       help="Operation mode: convert images, update markdown, cleanup originals, all, or build (optimized for CI/CD)")
    parser.add_argument("--clean-references", action="store_true", 
                       help="Use clean WebP references instead of picture elements with fallbacks")
    parser.add_argument("--quiet", action="store_true", help="Suppress verbose output")
    parser.add_argument("--inventory", action="store_true", help="Show image inventory and exit")
    
    args = parser.parse_args()
    
    docs_path = Path(args.docs_path)
    if not docs_path.exists():
        print(f"Error: {docs_path} does not exist")
        sys.exit(1)
    
    # Show inventory if requested
    if args.inventory:
        optimizer = ImageOptimizer(docs_path, args.quality, args.lossless, not args.quiet)
        inventory = optimizer.get_image_inventory(args.extensions + ['gif'])
        print(f"📁 Image Inventory for {docs_path}:")
        for img_type, count in inventory.items():
            print(f"   {img_type.upper()}: {count} files")
        return
    
    # Special build mode for CI/CD integration
    if args.mode == "build":
        optimize_for_build(docs_path, args.quiet)
        return
    
    optimizer = ImageOptimizer(docs_path, args.quality, args.lossless, not args.quiet)
    
    # Execute operations based on mode
    if args.mode in ["convert", "all"]:
        print("🔄 Converting images to WebP...")
        for ext in args.extensions:
            pattern = f"*.{ext}"
            images = list(docs_path.rglob(pattern))
            
            for image_path in images:
                optimizer.convert_to_webp(image_path)
    
    if args.mode in ["update", "all"]:
        print("\n📝 Updating markdown references...")
        optimizer.update_markdown_references(args.clean_references)
    
    if args.mode in ["cleanup", "all"]:
        optimizer.cleanup_original_images(args.extensions)
    
    optimizer.print_summary()

if __name__ == "__main__":
    main()
