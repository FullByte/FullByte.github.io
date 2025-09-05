#!/usr/bin/env python3
"""
Local development build script with image optimization
Usage: python build.py [--serve] [--clean] [--no-optimize]
"""

import argparse
import subprocess
import sys
from pathlib import Path

def run_command(cmd, description, quiet_logging=False):
    """Run a command and handle errors."""
    print(f"🔄 {description}...")
    try:
        env = None
        if quiet_logging:
            import os
            env = os.environ.copy()
            env['PYTHONWARNINGS'] = 'ignore'
            env['MKDOCS_QUIET'] = '1'
        
        if quiet_logging:
            result = subprocess.run(cmd, shell=True, check=True, text=True, env=env, 
                                  capture_output=True)
            
            if result.stdout:
                # Filter out the verbose git-revision-date messages
                lines = result.stdout.split('\n')
                filtered_lines = []
                for line in lines:
                    if not any(skip in line for skip in [
                        '[git-revision-date-localized-plugin]',
                        'has no git logs, using current timestamp',
                        'First revision timestamp is older than last revision timestamp',
                        'This can be due to a quirk in `git` follow behaviour',
                        '[RSS-plugin]: Dates could not be retrieved for page'
                    ]):
                        filtered_lines.append(line)
                
                clean_output = '\n'.join(filtered_lines).strip()
                if clean_output:
                    print(clean_output)
        else:
            result = subprocess.run(cmd, shell=True, check=True, text=True, env=env)
        
        print(f"✅ {description} completed")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Local MkDocs build with image optimization")
    parser.add_argument("--serve", action="store_true", help="Start development server after build")
    parser.add_argument("--clean", action="store_true", help="Clean build before starting")
    parser.add_argument("--no-optimize", action="store_true", help="Skip image optimization")
    parser.add_argument("--port", default="8000", help="Development server port")
    parser.add_argument("--host", default="127.0.0.1", help="Development server host")
    
    args = parser.parse_args()
    
    # Check if we're in the right directory
    if not Path("mkdocs.yml").exists():
        print("❌ mkdocs.yml not found. Please run this script from the project root.")
        sys.exit(1)
    
    # Clean build if requested
    if args.clean:
        if not run_command("mkdocs build --clean", "Cleaning previous build", quiet_logging=True):
            sys.exit(1)
    
    # Run image optimization unless skipped
    if not args.no_optimize:
        if not run_command("python image_optimizer.py --mode build", "Optimizing images"):
            print("⚠️ Image optimization failed, continuing with build...")
    
    # Generate site statistics
    if not run_command("python generate_stats.py --quiet", "Generating site statistics"):
        print("⚠️ Statistics generation failed, continuing with build...")
    
    # Build the site
    if not run_command("mkdocs build", "Building site", quiet_logging=True):
        sys.exit(1)
    
    # Serve if requested
    if args.serve:
        print(f"🚀 Starting development server on http://{args.host}:{args.port}")
        try:
            subprocess.run(f"mkdocs serve --dev-addr={args.host}:{args.port}", shell=True, check=True)
        except KeyboardInterrupt:
            print("\n👋 Development server stopped")
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to start development server: {e}")
            sys.exit(1)
    else:
        print("✅ Build completed successfully!")
        print("💡 Run 'python build.py --serve' to start the development server")

if __name__ == "__main__":
    main()
