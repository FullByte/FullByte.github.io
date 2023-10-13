# Tailscale

| What          | Where |
|---------------|-------|
| Official Page |       |
| Source        |       |
| Download      |       |
| Install       |       |

## Setup

You need to have tailscale running on the same version on all systems. Run this command to update on linux:

```sh
sudo apt-get update && sudo apt-get install tailscale
```

run this command to start tailscale

```sh
tailscale up
```

Once the VPN is working, it is possible to close ports open to the internet e.g. SSH or RDP and access the machines using the VPN instead.
