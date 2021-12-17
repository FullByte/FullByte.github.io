# ScoutSuite

 ``` sh
git clone https://github.com/nccgroup/ScoutSuite /opt/scoutsuite
cd /opt/scoutsuite
virtualenv -p python3 venv
. venv/bin/activate
pip3 install -r requirements.txt
pip3 install azure-cli
cat <<EOT > /usr/local/bin/scout.sh
#!/bin/sh
. /opt/scoutsuite/venv/bin/activate > /dev/null 2>&1 && /opt/scoutsuite/scout.py $@
EOT
chmod +x /usr/local/bin/scout.sh
exit
```
