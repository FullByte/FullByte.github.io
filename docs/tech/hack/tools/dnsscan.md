# Dnscan

wordlist-based DNS subdomain scanner

 ```sh
sudo apt install python3-dnspython 
sudo git clone https://github.com/rbsec/dnscan /opt/dnscan
sudo pip install -r /opt/dnscan/requirements.txt
sudo ln -s /opt/dnscan/dnscan.py /usr/local/bin/dnscan.py
```

Run example:

 ```sh
./dnscan.py -d dev-%%.example.org
```
