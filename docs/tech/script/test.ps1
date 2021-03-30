# Add a new input
$text = "Correct Horse Battery Staple"

# Create folder and prepare variables
$DesktopPath = [System.Environment]::GetFolderPath([System.Environment+SpecialFolder]::Desktop)
Set-Location -Path $DesktopPath
$folder = $text -replace " ","_"
$fullpath = $DesktopPath +  "/" + $folder
New-Item -Path $DesktopPath -Name ($text -replace " ","_") -ItemType "directory" -Force
Set-Location -Path $fullpath

# Run imagine for 60min
$job = Start-Job -ScriptBlock { imagine $input } -InputObject ("'" + $text + "'")
Start-Sleep -s 3600
Stop-Job $job

# Create Video
ffmpeg -framerate 5 -i "$folder.%06d.jpg" -c:v libx264 "$folder.mp4"
ffmpeg -i "$folder.mp4" -vf "fps=10,scale=512:-1:flags=lanczos" -vcodec libwebp -lossless 0 -compression_level 6 -q:v 50 -loop 0 -preset picture -an -vsync 0 "$folder.webp"