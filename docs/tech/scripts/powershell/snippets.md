# Snippets

## Registry

Example to read registry values:

``` ps1
Get-ChildItem -Path "HKCU:\Software\Microsoft\Office\Outlook\Addins"
Get-ChildItem -Path "HKLM:\Software\Microsoft\Office\Outlook\Addins"
```

## Add PATH

Add current working folder as PATH variable:

``` ps1
[Environment]::SetEnvironmentVariable("Path", (Get-Location).Path + ";" + [Environment]::GetEnvironmentVariable("Path","Machine"), "Machine")
```

## Media

One-liner to convert all PNG Images of a folder to JPG images:

``` ps1
Get-ChildItem -Path (Get-Location) -Filter *.png | ForEach-Object { $img=[System.Drawing.Image]::FromFile($_.FullName); $jpg=([System.IO.Path]::ChangeExtension($_.FullName, '.jpg')); $enc=[System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders()|?{$_.MimeType -eq 'image/jpeg'}; $par=New-Object System.Drawing.Imaging.EncoderParameters(1); $par.Param[0]=New-Object System.Drawing.Imaging.EncoderParameter([System.Drawing.Imaging.Encoder]::Quality,90); $img.Save($jpg,$enc,$par); $img.Dispose() }; Write-Output 'Conversion complete.'
```

## Netzwerk

Simple Webserver

Install Polaris (`Install-Module -Name Polaris -Scope CurrentUser`) and run this one-liner:

``` ps1
Import-Module Polaris; New-PolarisStaticRoute -RoutePath '' -FolderPath (Get-Location).Path -Force; Start-Polaris -Port 8888
```

### UDP

#### UDP Sender

``` ps1
$udpSender = New-Object System.Net.Sockets.UdpClient
$bytes = [System.Text.Encoding]::UTF8.GetBytes("Hallo vom Client")
$udpSender.Send($bytes, $bytes.Length, "1.2.3.5", 12345)
$udpSender.Close()
```

#### UDP Listener

``` ps1
$udpClient = New-Object System.Net.Sockets.UdpClient 12345
$remoteEP = New-Object System.Net.IPEndPoint ([System.Net.IPAddress]::Any, 0)

Write-Host "Lausche auf UDP-Port 12345..."

while ($true) {
    $data = $udpClient.Receive([ref]$remoteEP)
    $text = [System.Text.Encoding]::UTF8.GetString($data)
    Write-Host "Empfangen von $($remoteEP.Address): $text"
}
```

#### UDP Check

``` ps1
Get-NetUDPEndpoint | Select-Object -Property LocalAddress, LocalPort, OwningProcess | Sort-Object LocalPort
```

### With iPerf

UDP Download

``` ps1
iperf3.exe -c <server> -u -P 10 -4 -R
```

UDP Upload

``` ps1
iperf3.exe -c <server> -u -P 10 -4
```

### TCP

#### TCP Connect

``` ps1
try { (New-Object Net.Sockets.TcpClient).Connect("1.2.3.4", 7600); "offen" } catch { "zu" }
```

#### TCP Firewall check

``` ps1
$tcp = New-Object System.Net.Sockets.TcpClient
$tcp.ReceiveTimeout = 3000
$tcp.SendTimeout = 3000
$sw = [System.Diagnostics.Stopwatch]::StartNew()
try {
    $tcp.Connect("1.2.3.4", 7600)
    "Port offen"
} catch {
    $sw.Stop()
    if ($sw.ElapsedMilliseconds -ge 2500) {
        "Möglicherweise gefiltert (Timeout)"
    } else {
        "Port wahrscheinlich geschlossen (RST empfangen)"
    }
}
```

#### TCP Listener

``` ps1
$listener = [System.Net.Sockets.TcpListener]::Create(7600)
$listener.Start()
Write-Host "TCP-Listener läuft auf Port 7600..."

while ($true) {
    if ($listener.Pending()) {
        $client = $listener.AcceptTcpClient()
        Write-Host "Neue Verbindung: $($client.Client.RemoteEndPoint)"
        $client.Close()
    }
    Start-Sleep -Milliseconds 500
}
```

#### TCP Check

``` ps1
Get-NetTCPConnection -State Listen | Select-Object -Property LocalAddress, LocalPort, OwningProcess | Sort-Object LocalPort
```

#### TCP Check with iPerf

TCP Download

``` ps1
iperf3.exe -c <server> -P 10 -4 -R
```

TCP Upload

``` ps1
iperf3.exe -c <server> -P 10 -4
```

### Multicast

Checks

- Port must be allowed (check Firewall local or in network)
- Verify that the network infrastructure (switches, routers) allows multicast (no filtering/IGMP blocking).
- Ensure both sender and receiver are on the same LAN/subnet (unless you have multicast routing set up).
- Use a multicast address in the range 224.0.0.0 to 239.255.255.255

#### Listener

``` ps1
$groupAddress = "239.255.0.1"
$port = 5001

$udpClient = New-Object System.Net.Sockets.UdpClient
$localEp = New-Object System.Net.IPEndPoint ([System.Net.IPAddress]::Any, $port)
$udpClient.Client.SetSocketOption([System.Net.Sockets.SocketOptionLevel]::Socket, [System.Net.Sockets.SocketOptionName]::ReuseAddress, $true)
$udpClient.ExclusiveAddressUse = $false
$udpClient.Client.Bind($localEp)

$udpClient.JoinMulticastGroup([System.Net.IPAddress]::Parse($groupAddress))

Write-Host "Listening for multicast on $groupAddress:$port..."
while ($true) {
    $received = $udpClient.Receive([ref]$localEp)
    $text = [System.Text.Encoding]::UTF8.GetString($received)
    Write-Host "Received from $($localEp.Address): $text"
}
```

### Sender

``` ps1
$groupAddress = "239.255.0.1"
$port = 5001
$message = "Hello multicast from $(hostname)"
$remoteIp = [System.Net.IPAddress]::Parse($groupAddress)
$remoteEp = New-Object System.Net.IPEndPoint $remoteIp, $port

$udpClient = New-Object System.Net.Sockets.UdpClient
$bytes = [System.Text.Encoding]::UTF8.GetBytes($message)

for ($i = 1; $i -le 10; $i++) {
    $udpClient.Send($bytes, $bytes.Length, $remoteEp) | Out-Null
    Write-Host "Sent: $message"
    Start-Sleep -Seconds 1
}

$udpClient.Close()
```
