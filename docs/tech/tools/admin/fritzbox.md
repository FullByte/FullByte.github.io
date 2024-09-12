# Fritzbox

## Remote Reboot

``` bat
set IP=192.168.178.1
set FRITZUSER=rebootuser
set FRITZPW=rebootuserpw
set location=/upnp/control/deviceconfig
set uri=urn:dslforum-org:service:DeviceConfig:1
set action=Reboot

curl -k -m 5 --anyauth -u "%FRITZUSER%:%FRITZPW%" http://%IP%:49000%location% -H "Content-Type: text/xml; charset="utf-8"" -H "SoapAction:%uri%#%action%" -d "<?xml version='1.0' encoding='utf-8'?><s:Envelope s:encodingStyle='http://schemas.xmlsoap.org/soap/encoding/' xmlns:s='http://schemas.xmlsoap.org/soap/envelope/'><s:Body><u:Reboot xmlns:u='urn:dslforum-org:service:DeviceConfig:1'></u:Reboot></s:Body></s:Envelope>" -s > output.log 2>&1
```

## Log Network Traffic

Open <http://192.168.178.1/html/capture.html> and start logging traffic. The stored file can be viewed in Wireshark.
