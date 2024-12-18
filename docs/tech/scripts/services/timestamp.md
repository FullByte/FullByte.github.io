# Timestamp

Port 318 for PKIX Time Stamp Protocol (TSP) is used for time-stamping in cryptographic operations, ensuring that digital signatures or documents are bound to a specific time. This can help prove the existence of data at a particular moment. See details in RFC 3161.

While officially designated, this port is not widely used in practice for timestamping, as most time-stamping services operate over HTTPS (e.g., on port 443). Modern timestamp servers like the D-Trust service often use HTTPS-based endpoints instead.

## Test Timestamp server

Simple check:

- Windows: ```telnet <hostname> 318```
- Linux: ```nc -zv <hostname> 318```

### No Auth

Run this to create a sample.txt, request.tsq and send (via HTTP POST) that to the timestamp server

``` bat
echo "Test data for timestamping" > sample.txt
openssl ts -query -data sample.txt -no_nonce -sha256 -out request.tsq
curl --header "Content-Type: application/timestamp-query" --data-binary "@request.tsq" https://timestamp-service.d-trust.net/ -o response.tsr
openssl ts -reply -in response.tsr -text
```

Example output:

``` txt
Status: granted
Time: Dec 18 10:00:00 2024 GMT
Serial number: 123456789
Hash Algorithm: sha256
Signature Algorithm: sha256WithRSAEncryption
```

If you require authentication you will get an error like this:

``` html
<HTML><BODY>
Missing basic authentication in the received HTTP POST with Content-Type application/timestamp-query.
</BODY></HTML>
```

or

```txt
68910000:error:068000A8:asn1 encoding routines:asn1_check_tlen:wrong tag:crypto\asn1\tasn_dec.c:1188:
68910000:error:0688010A:asn1 encoding routines:asn1_item_embed_d2i:nested asn1 error:crypto\asn1\tasn_dec.c:349:Type=TS_RESP
```

### With Auth

``` sh
curl --header "Content-Type: application/timestamp-query" --user my_id:my_secret --data-binary "@request.tsq" https://timestamp-service.d-trust.net/ -o response.tsr
```
