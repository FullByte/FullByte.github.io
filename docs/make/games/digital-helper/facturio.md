# Facturio

Update server

``` sh
service factorio stop
sudo -u factorio wget https://factorio.com/get-download/stable/headless/linux64 -O /home/factorio/factorio_headless.tar.xz
sudo -u factorio tar -xvf /home/factorio/factorio_headless.tar.xz -C /home/factorio/
sudo -u factorio rsync -au /home/factorio/factorio/ /home/factorio/server/
service factorio start
rm /home/factorio/factorio_headless.tar.xz
rm -R /home/factorio/factorio/
```
