#!/usr/bin/env python3
"""
Media Path Checker for MkDocs
Finds and reports media files that might have path issues
"""

import os
import re
from pathlib import Path

def find_media_references(docs_dir="docs"):
    """Find all media references in markdown files."""
    docs_path = Path(docs_dir)
    issues = []
    media_refs = []
    
    # Find all markdown files
    md_files = list(docs_path.rglob("*.md"))
    
    # Patterns for media files
    audio_pattern = r'<audio[^>]*><source\s+src="([^"]+)"'
    video_pattern = r'<video[^>]*><source\s+src="([^"]+)"'
    img_pattern = r'!\[[^\]]*\]\(([^)]+)\)'
    html_img_pattern = r'<img[^>]*src="([^"]+)"'
    
    patterns = [
        ("audio", audio_pattern),
        ("video", video_pattern), 
        ("markdown_image", img_pattern),
        ("html_image", html_img_pattern)
    ]
    
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            relative_path = md_file.relative_to(docs_path)
            
            for media_type, pattern in patterns:
                matches = re.findall(pattern, content)
                for match in matches:
                    media_refs.append({
                        'file': str(relative_path),
                        'media_type': media_type,
                        'src': match,
                        'full_path': md_file
                    })
                    
                    # Check if referenced file exists
                    if not match.startswith(('http://', 'https://', '//')):
                        # Resolve relative path
                        if match.startswith('/'):
                            # Absolute path from docs root
                            media_file = docs_path / match.lstrip('/')
                        else:
                            # Relative path from current file
                            media_file = md_file.parent / match
                        
                        if not media_file.exists():
                            issues.append({
                                'file': str(relative_path),
                                'media_type': media_type,
                                'src': match,
                                'issue': 'File not found',
                                'expected_path': str(media_file)
                            })
        
        except Exception as e:
            print(f"Error reading {md_file}: {e}")
    
    return media_refs, issues

def main():
    print("🔍 Scanning for media references...")
    
    media_refs, issues = find_media_references()
    
    print(f"\n📊 Found {len(media_refs)} media references")
    
    if issues:
        print(f"\n❌ Found {len(issues)} potential issues:")
        for issue in issues:
            print(f"  File: {issue['file']}")
            print(f"  Type: {issue['media_type']}")
            print(f"  Source: {issue['src']}")
            print(f"  Issue: {issue['issue']}")
            print(f"  Expected: {issue['expected_path']}")
            print("-" * 40)
    else:
        print("\n✅ No path issues found!")
    
    # Group by media type
    by_type = {}
    for ref in media_refs:
        media_type = ref['media_type']
        if media_type not in by_type:
            by_type[media_type] = []
        by_type[media_type].append(ref)
    
    print(f"\n📈 Media breakdown:")
    for media_type, refs in by_type.items():
        print(f"  {media_type}: {len(refs)} references")
    
    return len(issues) == 0

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
