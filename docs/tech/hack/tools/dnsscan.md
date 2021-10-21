# Dnscan

wordlist-based DNS subdomain scanner

```shell
sudo apt install python3-dnspython 
sudo git clone https://github.com/rbsec/dnscan /opt/dnscan
sudo pip install -r /opt/dnscan/requirements.txt
sudo ln -s /opt/dnscan/dnscan.py /usr/local/bin/dnscan.py
```

Run example:

```shell
./dnscan.py -d dev-%%.example.org
```
