# MkDocs Build Script with Image Optimization
# Usage: .\build.ps1 [-Serve] [-Clean] [-NoOptimize] [-Port 8000] [-ServerHost "127.0.0.1"]

param(
    [switch]$Serve,
    [switch]$Clean, 
    [switch]$NoOptimize,
    [string]$Port = "8000",
    [string]$ServerHost = "127.0.0.1"
)

function Invoke-QuietMkDocs {
    param([string]$Command, [string]$Description)
    
    Write-Step $Description
    try {
        # Capture output to filter verbose messages
        $output = & cmd /c "$Command 2>&1"
        
        # Filter out verbose git plugin messages
        $filteredOutput = $output | Where-Object {
            $_ -notmatch '\[git-revision-date-localized-plugin\]' -and
            $_ -notmatch 'has no git logs, using current timestamp' -and
            $_ -notmatch 'First revision timestamp is older than last revision timestamp' -and
            $_ -notmatch 'This can be due to a quirk in.*git.*follow behaviour' -and
            $_ -notmatch '\[RSS-plugin\]: Dates could not be retrieved for page'
        }
        
        # Output filtered results
        $filteredOutput | ForEach-Object { Write-Host $_ }
        
        Write-Success "$Description completed"
        return $true
    }
    catch {
        Write-Error "$Description failed: $_"
        return $false
    }
}

function Write-Step {
    param([string]$Message)
    Write-Host "🔄 $Message..." -ForegroundColor Cyan
}

function Write-Success {
    param([string]$Message)
    Write-Host "✅ $Message" -ForegroundColor Green
}

function Write-Error {
    param([string]$Message)
    Write-Host "❌ $Message" -ForegroundColor Red
}

function Write-Warning {
    param([string]$Message)
    Write-Host "⚠️ $Message" -ForegroundColor Yellow
}

# Check if we're in the right directory
if (-not (Test-Path "mkdocs.yml")) {
    Write-Error "mkdocs.yml not found. Please run this script from the project root."
    exit 1
}

# Clean build if requested
if ($Clean) {
    if (-not (Invoke-QuietMkDocs "mkdocs build --clean" "Cleaning previous build")) {
        exit 1
    }
}

# Run image optimization unless skipped
if (-not $NoOptimize) {
    Write-Step "Optimizing images"
    try {
        & python image_optimizer.py --mode build
        Write-Success "Image optimization completed"
    }
    catch {
        Write-Warning "Image optimization failed, continuing with build..."
    }
}

# Generate site statistics
Write-Step "Generating site statistics"
try {
    & python generate_stats.py --quiet
    Write-Success "Site statistics generated"
}
catch {
    Write-Warning "Statistics generation failed, continuing with build..."
}

# Build the site
if (-not (Invoke-QuietMkDocs "mkdocs build" "Building site")) {
    exit 1
}

# Serve if requested
if ($Serve) {
    Write-Host "🚀 Starting development server on http://$ServerHost`:$Port" -ForegroundColor Magenta
    try {
        & mkdocs serve --dev-addr="$ServerHost`:$Port"
    }
    catch {
        if ($_.Exception.Message -like "*KeyboardInterrupt*" -or $_.Exception.Message -like "*interrupted*") {
            Write-Host "`n👋 Development server stopped" -ForegroundColor Yellow
        }
        else {
            Write-Error "Failed to start development server: $_"
            exit 1
        }
    }
}
else {
    Write-Success "Build completed successfully!"
    Write-Host "💡 Run '.\build.ps1 -Serve' to start the development server" -ForegroundColor Blue
}
