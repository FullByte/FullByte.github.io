# Lightning Fast

These notes are from a challenge I did @[hackthebox](https://hackthebox.com) called [LightningFast](https://app.hackthebox.com/challenges/lightningfast).

Download the Files and start the machine ...

Playing the game requires connecting to the machine we started.

The score is stored even if the game is stopped.
It could be stored locally.... or transmitted to our server.

Lets run wireshark, filter for ```ip.addr==206.189.117.48```, search for a POST and follow the HTTP stream.

Once done we get an output like this:

``` http
POST /moupNn HTTP/1.1
Host: 206.189.117.48:31690
User-Agent: UnityPlayer/2021.1.12f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)
Accept: /
Accept-Encoding: identity
Content-Type: application/json
X-Unity-Version: 2021.1.12f1
Content-Length: 14

{"score": 161}HTTP/1.1 200 OK
X-Powered-By: Express
Content-Type: application/json; charset=utf-8
Content-Length: 13
ETag: W/"d-t6O51JE27cWM115Auh24Li81kk8"
Date: Thu, 01 Sep 2022 19:05:23 GMT
Connection: keep-alive
Keep-Alive: timeout=5

{"score":161}GET /endpoints HTTP/1.1
Host: 206.189.117.48:31690
User-Agent: UnityPlayer/2021.1.12f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)
Accept: /
Accept-Encoding: identity
X-Unity-Version: 2021.1.12f1

HTTP/1.1 200 OK
X-Powered-By: Express
Content-Type: application/json; charset=utf-8
Content-Length: 37
ETag: W/"25-U7Gi7IARGv2RpF3sXmCE8Zala8Q"
Date: Thu, 01 Sep 2022 19:05:23 GMT
Connection: keep-alive
Keep-Alive: timeout=5

{"getter":"xLsFrn","setter":"moupNn"}GET /xLsFrn HTTP/1.1
Host: 206.189.117.48:31690
User-Agent: UnityPlayer/2021.1.12f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)
Accept: /
Accept-Encoding: identity
X-Unity-Version: 2021.1.12f1

HTTP/1.1 200 OK
X-Powered-By: Express
Content-Type: application/json; charset=utf-8
Content-Length: 13
ETag: W/"d-t6O51JE27cWM115Auh24Li81kk8"
Date: Thu, 01 Sep 2022 19:05:26 GMT
Connection: keep-alive
Keep-Alive: timeout=5

{"score":161}
```

The first bit is already interesting: With this information we can extract what is need to send a new POST command with curl e.g. set the score to 666:

``` sh
curl -XPOST -H 'X-Unity-Version: 2021.1.12f1' -H "Content-type: application/json" -d '{"score": 666}' 'http://206.189.117.48:31690/moupNn'
```

Once we start a new game the score continues at 666.

There are many options to send a POST request... lets use telnet to achieve the required score for the flag :D

``` cmd
telnet
Microsoft Telnet> open 206.189.117.48 31690
```

Then just paste a slightly adjusted POST command we got from wireshark (make sure to match Content-Length with your json):

``` telnet
POST /moupNn HTTP/1.1
Host: 206.189.117.48:31690
User-Agent: UnityPlayer/2021.1.12f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)
Accept: /
Accept-Encoding: identity
Content-Type: application/json
X-Unity-Version: 2021.1.12f1
Content-Length: 18

{"score": 1000000}
```

Once the score is set to 1000000 we get to see the flag in the store ^^
