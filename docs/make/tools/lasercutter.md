# Laser cutter

## Boxes.py

- Website: <https://www.festi.info/boxes.py/>
- Github: <https://github.com/florianfesti/boxes>

"Boxes.py" is an [online](https://www.festi.info/boxes.py/index.html) and [Inkscape plug-in](https://github.com/florianfesti/boxes) with ready-to-use, fully parametrized generators for various boxes.

Boxes is great for laser cutters that are powerful enough to cut through wood:

Sofar I tested cuts with these fiberboard types:

- 2,5 mm MDF
- 3,0 mm MDF
- 3,0 mm HDF

With these laser cutters (both work well):

- [Epilog Zing 6040](https://www.epiloglaser.de/)
- [Trotec Speedy 360](https://www.troteclaser.com)

This is a script I wrote to install and run boxes locally on Windows 10:

One-liner executing the gist I created:

```powershell
iex ((New-Object System.Net.WebClient).DownloadString('https://gist.githubusercontent.com/FullByte/f0140dda330ffb19cee4e0cf24a0cdfd/raw/5b81224d02959514b65c4216ee585c1cfa1b2861/%25E2%2580%258B%2520Start-Boxes.ps1'))
```

This is the script to get all the requirements installed, download the code and run a local webserver serving boxes py:

```powershell
#Requires -RunAsAdministrator

# Install/Update tools
if (!(Test-Path "$($env:ProgramData)\chocolatey\choco.exe")) { Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1')) }
choco install -y python git
python -m pip install --upgrade pip 
pip install Markdown lxml affine
    
# Install/Update boxes
$boxes = "${PSScriptRoot}\boxes" 
if (Test-Path $boxes) { git --work-tree=$boxes --git-dir=$boxes\.git pull }
else { git clone https://github.com/florianfesti/boxes.git $boxes } 
        
# Run Boxes
Start-Process python $boxes\scripts\boxesserver
Start-Process http://localhost:8000
```

## Project Ideas

Everything

- Instructables <https://www.instructables.com/>
- Make <https://make.co/>
- Pintrest <https://www.pinterest.de/>
- Hackster <https://www.hackster.io/projects?ref=topnav>

Laser cutter & CNC

- boxes.py <https://www.festi.info/boxes.py/>
- Laser Templates <https://laser-templates.com/>
- Templatemaker <https://www.templatemaker.nl>
- <https://www.dxf-downloads.de/>
- <https://dxf-downloads.com>
- <https://de.makercase.com/>
- <http://jeromeleary.com/laser/>
- maze generator <http://www.mazegenerator.net/>
- Create Puzzle <https://cdn.rawgit.com/Draradech/35d36347312ca6d0887aa7d55f366e30/raw/b04cf9cd63a59571910cb226226ce2b3ed46af46/jigsaw.html>

## Devices

### EpilogZing 6040

The Lasercutter EpilogZing 6040 is a 40 Watt CO2-Laser.

Max size: 600mm x 300mm.

#### 3mm HDF

Engrave (Raster):

- Job Type: Raster
- Speed: 58%
- Power: 50%
- Freq: 2500 Hz

Cut (Vektor):

- Job Type: Vector
- Speed: 50%
- Power: 100%
- Freq: 2500 Hz

!(epilog-zing-printer-settings)[_epilog-zing-printer-settings.png]

#### 4mm fleece

Engrave (Raster):

- Job Type: Raster
- Speed: 100%
- Power: 36%
- Freq: 5000 Hz

Cut (Vektor, [Example Cut](_fleece_example_cut.png)):

- Job Type: Vector
- Speed: 100%
- Power: 62%
- Freq: 5000 Hz

### Trotec Speedy 360

#### 4mm MDF

- Power: 80,00
- Velocity: 1,00
- PPI/Hz: 1000
- Runs: 3

#### 5mm MDF

Power: 100
Velocity: 3
PPI/Hz: 1000
Runs: 2
