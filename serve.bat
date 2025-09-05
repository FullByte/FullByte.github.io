@echo off
REM Simple MkDocs development server launcher
REM Usage: serve.bat [port]

set PORT=%1
if "%PORT%"=="" set PORT=8000

echo 🚀 Starting MkDocs development server on port %PORT%...
python serve.py --port %PORT%
