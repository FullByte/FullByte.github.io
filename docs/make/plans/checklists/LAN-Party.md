# LAN Party

Playing games locally in a network requires some preparation and some tools help get organized. Here are some notes I made on the topic :)

Preparing:

- Make a list of all games that will be played and make sure all have downloaded, updated and started the game atleast once prior to the LAN party

Games Equipment

- Headphones

On Site:

- Make sure there is enough Poweradapters, Cables, Charis, Tables

## Scan and Test Network

Have a look if you can see everyone in the LAN:

- You can scan the network to see who else is already visible: ```nmap -sC -sV 192.168.178.0/24```
- And/Or run a simple ARP command to see who you already see: ```arp -a```
- Test a connection to a given IP e.g.: ```Test-NetConnection -ComputerName 192.168.178.41 -InformationLevel "Detailed"``` (optionally add a port e.g. "-Port 3389")

## Games

A list of games that are free and fun:

| Game                                                                            | Notes                                                   |
|---------------------------------------------------------------------------------|---------------------------------------------------------|
| [Trackmania](https://www.trackmania.com/)                                       | Host requires standard membership and maps              |
| [CS GO](https://store.steampowered.com/app/730/CounterStrike_Global_Offensive/) |                                                         |
| [Blobby Volleyball](http://blobbyvolley.de/)                                    | Setup a tournament and distribute the zipped game prior |
| [Rocket League](https://www.rocketleague.com/)                                  |                                                         |
| [StarCraft II](https://starcraft2.com)                                          |                                                         |
| [Warzone 2100](https://wz2100.net/)                                             |                                                         |
| [armagetronad](http://www.armagetronad.org)                                     |                                                         |
| [xonotic](https://xonotic.org/)                                                 |                                                         |
| [Minetest](https://www.minetest.net/)                                           |                                                         |
| [The Battle for Wesnoth](https://www.wesnoth.org)                               |                                                         |
| [SuperTuxKart](https://supertuxkart.net/)                                       | Racing game simular to Mario Cart                       |
| [Tee Worlds](https://www.teeworlds.com/)                                        | 2D Jump and Run Shooter                                 |

Modern games that work well in LAN

- Age of Empires II Definitive Edition

Nice old games

- Quake III Arena
- Counterstrike 1.6
- Unreal Tournament
- Warcraft III

## Share Files

Easiest way to share files ist by ziping whatever you want to share first.

You can run a simple webserver using python: ``` python -m http.server 8080```

## Windows Firewall

Check your inbound rules and possibly add a rule/remove a restricition:

``` ps1
Get-NetFirewallRule | Where { $_.Enabled -eq 'True' -and $_.Direction -eq 'Inbound' } | Select-Object DisplayName, Direction, Action, Profile | FT
```

Alternativly, add firewall rules to allow all local traffic (same subnet):

``` ps1
New-NetFirewallRule -DisplayName "Allow LAN Party OUT" -Direction Outbound -LocalPort 1-10000 -Protocol TCP -RemoteAddress LocalSubnet -Action Allow
New-NetFirewallRule -DisplayName "Allow LAN Party IN" -Direction Inbound -LocalPort 1-10000 -Protocol TCP -RemoteAddress LocalSubnet -Action Allow
```

Remove the rules from above:

``` ps1
Remove-NetFirewallRule -DisplayName "Allow LAN Party OUT"
Remove-NetFirewallRule -DisplayName "Allow LAN Party IN"
```

Or, if nothing helps, disable the Firewall for your current profile during the LAN event: ```netsh advfirewall set currentprofile state off```

You can reset your firewall settings as follows. Windows will then ask you whenever you start an application what to do with this currently blocked application.

``` ps1
(New-Object -ComObject HNetCfg.FwPolicy2).RestoreLocalFirewallDefaults()
```

### Services

- Set up a tournament: <https://www.toornament.com>
- More counters: <https://scorecount.com/>
