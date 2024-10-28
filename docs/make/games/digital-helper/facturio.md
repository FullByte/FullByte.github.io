# Facturio

``` sh
service factorio stop
sudo -u factorio bash
wget https://factorio.com/get-download/stable/headless/linux64 -O factorio_headless.tar.xz
tar -xvf factorio_headless.tar.xz
rsync -au factorio/ server/
service factorio start
```