# Admin

## Sysinternals

Info

| What          | Where                                                                                           |
|---------------|-------------------------------------------------------------------------------------------------|
| Official Page |                                                                                                 |
| Download      | <https://docs.microsoft.com/sysinternals/>                                                      |
| Install       | <https://www.microsoft.com/en-us/p/sysinternals-suite/9p7knl5rwt25#activetab=pivot:overviewtab> |

### PsExec

Add User to log on remotely:
LocalUser = evtl. ein service account z.B. für updates/monitoring/…
Server = name des Zielservers

``` ps1
PsExec.exe \\Server -u "Server\\LocalUser" -p "LocalUserPW" net user testuser2 Passw0rd1 /add
PsExec.exe \\Server -u "Server\\LocalUser" -p "LocalUserPW" net localgroup "Administrators" testuser /add
PsExec.exe \\Server -u "Server\\LocalUser" -p "LocalUserPW" net localgroup "Remote Desktop Users" testuser /add
```

### Sysinternals live

Run sysinternals tools from the explorer

``` ps1
\\live.sysinternals.com\tools\procexp.exe
```

Or zoom ...

``` ps1
\\live.sysinternals.com\tools\ZoomIt.exe
```

You get the idea :)

## Server Apps

More: <https://github.com/awesome-selfhosted/awesome-selfhosted>

### Helper

- endoflife date <https://endoflife.date/>

### Infrastructure

- <https://github.com/mizzy/serverspec>
- <https://github.com/aelsabbahy/goss>
- <https://github.com/argoproj/argo-cd>

### Services

- Reliable, High Performance TCP/HTTP Load Balancer <https://www.haproxy.org/>
- Backup with Restic <https://restic.net/>
- NetBox is an IP address management (IPAM) and data center infrastructure management (DCIM) tool <https://github.com/netbox-community/netbox>
- A private network system that uses WireGuard under the hood. <https://github.com/tonarino/innernet>

### Smart Home

- <https://www.ai-cam.app/>
- <https://shinobi.video/>
- <https://pi-hole.net/>
- <https://sandstorm.io>
- <https://truenas.de/>
- <https://docs.pivpn.io/>

### Web Store

#### opencart

- Source: <https://github.com/opencart/opencart>
- Website: <https://www.opencart.com>

#### PrestaShop

- Source: <https://github.com/PrestaShop/PrestaShop>
- Website: <https://www.prestashop.com/de>

#### woocommerce

- Source: <https://github.com/woocommerce/woocommerce>
- Website: <https://woocommerce.com/>

#### nopCommerce

- Source: <https://github.com/nopSolutions/nopCommerce>
- Website: <https://www.nopcommerce.com/>
