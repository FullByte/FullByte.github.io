#!/usr/bin/env python3
"""
Robust MkDocs development server with error handling
"""

import subprocess
import sys
import time
import os
from pathlib import Path

def run_mkdocs_serve(host="127.0.0.1", port="8000", clean=False):
    """Run MkDocs serve with proper error handling."""
    
    # Check if we're in the right directory
    if not Path("mkdocs.yml").exists():
        print("❌ mkdocs.yml not found. Please run this script from the project root.")
        sys.exit(1)
    
    # Set environment variables for quieter output
    env = os.environ.copy()
    env['MKDOCS_QUIET'] = '1'
    env['PYTHONWARNINGS'] = 'ignore'
    
    # Build command - use the virtual environment mkdocs
    venv_mkdocs = Path(".venv/Scripts/mkdocs.exe")
    if venv_mkdocs.exists():
        mkdocs_cmd = str(venv_mkdocs)
    else:
        mkdocs_cmd = "mkdocs"
    
    cmd = f'"{mkdocs_cmd}" serve --dev-addr={host}:{port}'
    if clean:
        cmd += " --clean"
    
    print(f"🚀 Starting MkDocs development server...")
    print(f"📍 Server will be available at: http://{host}:{port}")
    print("🔄 Building documentation (this may take a moment)...")
    print("💡 Press Ctrl+C to stop the server")
    print("-" * 50)
    
    max_retries = 3
    retry_count = 0
    
    while retry_count < max_retries:
        try:
            # Start the process
            process = subprocess.Popen(
                cmd,
                shell=True,
                env=env,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                universal_newlines=True,
                bufsize=1
            )
            
            # Stream output with filtering
            if process.stdout:
                for line in iter(process.stdout.readline, ''):
                    # Filter out verbose messages
                    if not any(skip in line for skip in [
                        '[git-revision-date-localized-plugin]',
                        'First revision timestamp is older than last revision timestamp',
                        'This can be due to a quirk in',
                        '[RSS-plugin]: Dates could not be retrieved for page',
                        'has no git logs, using current timestamp'
                    ]):
                        print(line, end='')
                        
                        # Check if server is ready
                        if "Serving on http://" in line:
                            print("✅ Server is ready!")
                            print("🌐 Open your browser and navigate to the URL above")
                            print("-" * 50)
            
            process.wait()
            break
            
        except KeyboardInterrupt:
            print("\n👋 Development server stopped by user")
            if process:
                process.terminate()
            break
            
        except subprocess.CalledProcessError as e:
            retry_count += 1
            print(f"❌ Server failed (attempt {retry_count}/{max_retries}): {e}")
            
            if retry_count < max_retries:
                print("🔄 Retrying in 2 seconds...")
                time.sleep(2)
            else:
                print("❌ Failed to start server after multiple attempts")
                sys.exit(1)
                
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            sys.exit(1)

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Robust MkDocs development server")
    parser.add_argument("--host", default="127.0.0.1", help="Host to bind to")
    parser.add_argument("--port", default="8000", help="Port to bind to")
    parser.add_argument("--clean", action="store_true", help="Clean build before serving")
    
    args = parser.parse_args()
    
    run_mkdocs_serve(args.host, args.port, args.clean)

if __name__ == "__main__":
    main()
