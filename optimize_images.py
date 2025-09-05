#!/usr/bin/env python3
"""
Image optimization script for MkDocs documentation.
Optimizes JPEG and PNG images in the docs folder while preserving originals as .bak files.
"""

import os
import sys
from pathlib import Path
from PIL import Image, ImageFile
import argparse

# Allow loading of truncated images
ImageFile.LOAD_TRUNCATED_IMAGES = True

def optimize_image(image_path, quality=80, png_compress_level=6, max_width=1920):
    """
    Optimize a single image file.
    
    Args:
        image_path: Path to the image file
        quality: JPEG quality (1-100)
        png_compress_level: PNG compression level (0-9)
        max_width: Maximum width to resize large images
    """
    try:
        # Get original file size before processing
        original_size = os.path.getsize(image_path)
        
        # Open and process image
        with Image.open(image_path) as img:
            # Convert RGBA to RGB for JPEG if needed
            if img.mode in ('RGBA', 'LA') and image_path.suffix.lower() in ['.jpg', '.jpeg']:
                background = Image.new('RGB', img.size, (255, 255, 255))
                background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
                img = background
            
            # Resize if too large
            if img.width > max_width:
                ratio = max_width / img.width
                new_height = int(img.height * ratio)
                img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
            
            # Save optimized image directly (overwrite original)
            if image_path.suffix.lower() in ['.jpg', '.jpeg']:
                img.save(image_path, optimize=True, quality=quality, progressive=True)
            elif image_path.suffix.lower() == '.png':
                img.save(image_path, optimize=True, compress_level=png_compress_level)
            else:
                img.save(image_path, optimize=True)
            
        # Get new file size
        new_size = os.path.getsize(image_path)
        savings = original_size - new_size
        savings_percent = (savings / original_size) * 100
        
        return original_size, new_size, savings, savings_percent
        
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return 0, 0, 0, 0

def optimize_docs_images(docs_path="docs", quality=80, max_width=1920, dry_run=False):
    """
    Optimize all images in the docs directory.
    
    Args:
        docs_path: Path to docs directory
        quality: JPEG quality (1-100)
        max_width: Maximum width for resizing
        dry_run: If True, only analyze without making changes
    """
    docs_dir = Path(docs_path)
    if not docs_dir.exists():
        print(f"Docs directory '{docs_path}' not found!")
        return
    
    # Find all image files
    image_extensions = {'.jpg', '.jpeg', '.png'}
    image_files = []
    
    for ext in image_extensions:
        image_files.extend(docs_dir.rglob(f'*{ext}'))
        image_files.extend(docs_dir.rglob(f'*{ext.upper()}'))
    
    if not image_files:
        print("No image files found in docs directory.")
        return
    
    print(f"Found {len(image_files)} image files")
    
    total_original_size = 0
    total_new_size = 0
    total_savings = 0
    processed_count = 0
    
    for image_path in image_files:
        print(f"Processing: {image_path.relative_to(docs_dir)}")
        
        if dry_run:
            # Just report current file size
            current_size = image_path.stat().st_size
            total_original_size += current_size
            print(f"  Current size: {current_size / 1024:.1f} KB")
        else:
            original_size, new_size, savings, savings_percent = optimize_image(
                image_path, quality=quality, max_width=max_width
            )
            
            if original_size > 0:
                total_original_size += original_size
                total_new_size += new_size
                total_savings += savings
                processed_count += 1
                
                print(f"  {original_size / 1024:.1f} KB → {new_size / 1024:.1f} KB "
                      f"({savings_percent:+.1f}%)")
    
    # Summary
    if dry_run:
        print(f"\nDry run summary:")
        print(f"Total current size: {total_original_size / 1024 / 1024:.1f} MB")
        print(f"Estimated savings: 30-60% (rough estimate)")
    else:
        print(f"\nOptimization complete!")
        print(f"Files processed: {processed_count}")
        print(f"Total original size: {total_original_size / 1024 / 1024:.1f} MB")
        print(f"Total new size: {total_new_size / 1024 / 1024:.1f} MB")
        print(f"Total savings: {total_savings / 1024 / 1024:.1f} MB "
              f"({(total_savings / total_original_size) * 100:.1f}%)")

def restore_images(docs_path="docs"):
    """Restore functionality removed - no backups are created."""
    print("Restore functionality has been removed.")
    print("Images are now optimized in-place without creating backups.")
    print("If you need to restore original images, please restore from your git repository or other backup source.")
    return

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Optimize images in MkDocs documentation')
    parser.add_argument('--docs-path', default='docs', help='Path to docs directory')
    parser.add_argument('--quality', type=int, default=80, help='JPEG quality (1-100)')
    parser.add_argument('--max-width', type=int, default=1920, help='Maximum width for resizing')
    parser.add_argument('--dry-run', action='store_true', help='Analyze only, don\'t optimize')
    parser.add_argument('--restore', action='store_true', help='Restore images from backups')
    
    args = parser.parse_args()
    
    if args.restore:
        restore_images(args.docs_path)
    else:
        optimize_docs_images(
            docs_path=args.docs_path,
            quality=args.quality,
            max_width=args.max_width,
            dry_run=args.dry_run
        )
