# Robust MkDocs Development Server for Windows
# Usage: .\serve.ps1 [-Port 8000] [-Host "127.0.0.1"] [-Clean]

param(
    [string]$Port = "8000",
    [string]$ServerHost = "127.0.0.1",
    [switch]$Clean
)

function Write-Step {
    param([string]$Message)
    Write-Host "🔄 $Message" -ForegroundColor Cyan
}

function Write-Success {
    param([string]$Message)
    Write-Host "✅ $Message" -ForegroundColor Green
}

function Write-Info {
    param([string]$Message)
    Write-Host "💡 $Message" -ForegroundColor Blue
}

function Write-ServerReady {
    Write-Host "✅ Server is ready!" -ForegroundColor Green
    Write-Host "🌐 Open your browser and navigate to the URL above" -ForegroundColor Magenta
    Write-Host ("-" * 50) -ForegroundColor Gray
}

# Check if we're in the right directory
if (-not (Test-Path "mkdocs.yml")) {
    Write-Host "❌ mkdocs.yml not found. Please run this script from the project root." -ForegroundColor Red
    exit 1
}

# Find MkDocs executable
$mkdocsPath = ".\.venv\Scripts\mkdocs.exe"
if (-not (Test-Path $mkdocsPath)) {
    $mkdocsPath = "mkdocs"
}

# Build command
$cmd = "& `"$mkdocsPath`" serve --dev-addr=$ServerHost`:$Port"
if ($Clean) {
    $cmd += " --clean"
}

Write-Host "🚀 Starting MkDocs development server..." -ForegroundColor Magenta
Write-Host "📍 Server will be available at: http://$ServerHost`:$Port" -ForegroundColor Yellow
Write-Host "🔄 Building documentation (this may take a moment)..." -ForegroundColor Cyan
Write-Info "Press Ctrl+C to stop the server"
Write-Host ("-" * 50) -ForegroundColor Gray

# Set environment for quieter output
$env:MKDOCS_QUIET = "1"
$env:PYTHONWARNINGS = "ignore"

try {
    # Start the process and filter output
    $pinfo = New-Object System.Diagnostics.ProcessStartInfo
    $pinfo.FileName = "powershell.exe"
    $pinfo.Arguments = "-Command `"$cmd`""
    $pinfo.UseShellExecute = $false
    $pinfo.RedirectStandardOutput = $true
    $pinfo.RedirectStandardError = $true
    $pinfo.CreateNoWindow = $true
    
    $process = New-Object System.Diagnostics.Process
    $process.StartInfo = $pinfo
    $process.Start() | Out-Null
    
    $serverReady = $false
    
    # Read output line by line
    while (!$process.StandardOutput.EndOfStream) {
        $line = $process.StandardOutput.ReadLine()
        
        # Filter out verbose messages
        if ($line -notmatch 'git-revision-date-localized-plugin' -and
            $line -notmatch 'First revision timestamp is older than last revision timestamp' -and
            $line -notmatch 'This can be due to a quirk in' -and
            $line -notmatch 'RSS-plugin.*Dates could not be retrieved for page' -and
            $line -notmatch 'has no git logs, using current timestamp') {
            
            Write-Host $line
            
            # Check if server is ready
            if ($line -match "Serving on http://") {
                if (-not $serverReady) {
                    Write-ServerReady
                    $serverReady = $true
                }
            }
        }
    }
    
    $process.WaitForExit()
}
catch {
    if ($_.Exception.Message -like "*KeyboardInterrupt*" -or $_.Exception.Message -like "*interrupted*") {
        Write-Host "`n👋 Development server stopped by user" -ForegroundColor Yellow
    }
    else {
        Write-Host "❌ Server error: $_" -ForegroundColor Red
        exit 1
    }
}
finally {
    if ($process -and !$process.HasExited) {
        $process.Kill()
    }
}
