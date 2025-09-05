#!/usr/bin/env python3
"""
Pre-build image optimization hook for MkDocs
Automatically runs before MkDocs build to optimize any new images
"""

import sys
import subprocess
from pathlib import Path

def run_image_optimization():
    """Run image optimization before build."""
    try:
        # Import and run the optimizer directly
        from image_optimizer import optimize_for_build
        
        print("🖼️ Running pre-build image optimization...")
        has_changes = optimize_for_build("docs", quiet=False)
        
        if has_changes:
            print("✅ Image optimization completed with changes")
        else:
            print("✅ No new images to optimize")
            
        return True
        
    except ImportError:
        # Fallback to subprocess if import fails
        try:
            result = subprocess.run([
                sys.executable, "image_optimizer.py", 
                "--mode", "build", 
                "--docs-path", "docs"
            ], check=True, capture_output=True, text=True)
            
            print(result.stdout)
            if result.stderr:
                print(result.stderr)
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Image optimization failed: {e}")
            print(f"stdout: {e.stdout}")
            print(f"stderr: {e.stderr}")
            return False
        except FileNotFoundError:
            print("⚠️ image_optimizer.py not found, skipping image optimization")
            return True

if __name__ == "__main__":
    success = run_image_optimization()
    sys.exit(0 if success else 1)
