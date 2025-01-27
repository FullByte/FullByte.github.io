# Protocols

## HTTP

### Return Codes

HTTP return codes

| Code | Message                                | RFC                            |
| ---- | -------------------------------------- | ------------------------------ |
| 100  | Continue                               | RFC7231                        |
| 101  | Switching Protocols                    | RFC7231                        |
| 102  | Processing                             | RFC2518                        |
| 103  | Early Hints                            | RFC8297                        |
| 200  | OK                                     | RFC7231                        |
| 201  | Created                                | RFC7231                        |
| 202  | Accepted                               | RFC7231                        |
| 203  | Non-Authoritative Information          | RFC7231                        |
| 204  | No Content                             | RFC7231                        |
| 205  | Reset Content                          | RFC7231                        |
| 206  | Partial Content                        | RFC7231                        |
| 207  | Multi-Status                           | RFC4918                        |
| 208  | Already Reported                       | RFC5842                        |
| 226  | IM Used                                | RFC3229                        |
| 300  | Multiple Choices                       | RFC7231                        |
| 301  | Moved Permanently                      | RFC7231                        |
| 302  | Found                                  | RFC7231                        |
| 303  | See Other                              | RFC7231                        |
| 304  | Not Modified                           | RFC7231                        |
| 305  | Use Proxy                              | RFC7231                        |
| 306  | Reserved                               | RFC7231                        |
| 307  | Temporary Redirect                     | RFC7231                        |
| 308  | Permanent Redirect                     | RFC-reschke-http-status-308-07 |
| 400  | Bad Request                            | RFC7231                        |
| 401  | Unauthorized                           | RFC7231                        |
| 402  | Payment Required                       | RFC7231                        |
| 403  | Forbidden                              | RFC7231                        |
| 404  | Not Found                              | RFC7231                        |
| 405  | Method Not Allowed                     | RFC7231                        |
| 406  | Not Acceptable                         | RFC7231                        |
| 407  | Proxy Authentication Required          | RFC7231                        |
| 408  | Request Timeout                        | RFC7231                        |
| 409  | Conflict                               | RFC7231                        |
| 410  | Gone                                   | RFC7231                        |
| 411  | Length Required                        | RFC7231                        |
| 412  | Precondition Failed                    | RFC7231                        |
| 413  | Request Entity Too Large               | RFC7231                        |
| 414  | Request-URI Too Long                   | RFC7231                        |
| 415  | Unsupported Media Type                 | RFC7231                        |
| 416  | Requested Range Not Satisfiable        | RFC7231                        |
| 417  | Expectation Failed                     | RFC7231                        |
| 418  | I'm a teapot                           | RFC2324                        |
| 421  | Misdirected Request                    | RFC7540                        |
| 422  | Unprocessable Entity                   | RFC4918                        |
| 423  | Locked                                 | RFC4918                        |
| 424  | Failed Dependency                      | RFC4918                        |
| 425  | Too Early                              | RFC8470                        |
| 426  | Upgrade Required                       | RFC2817                        |
| 428  | Precondition Required                  | RFC6585                        |
| 429  | Too Many Requests                      | RFC6585                        |
| 431  | Request Header Fields Too Large        | RFC6585                        |
| 451  | Unavailable For Legal Reasons          | RFC7725                        |
| 500  | Internal Server Error                  | RFC7231                        |
| 501  | Not Implemented                        | RFC7231                        |
| 502  | Bad Gateway                            | RFC7231                        |
| 503  | Service Unavailable                    | RFC7231                        |
| 504  | Gateway Timeout                        | RFC7231                        |
| 505  | HTTP Version Not Supported             | RFC7231                        |
| 506  | Variant Also Negotiates (Experimental) | RFC2295                        |
| 507  | Insufficient Storage                   | RFC4918                        |
| 508  | Loop Detected                          | RFC5842                        |
| 510  | Not Extended                           | RFC2774                        |
| 511  | Network Authentication Required        | RFC6585                        |

Animal friendly status code responses:

- <https://httpstatusdogs.com/>
- <https://http.cat/>

## SMTP

<https://www.iana.org/assignments/smtp-enhanced-status-codes/smtp-enhanced-status-codes.xhtml>

<https://en.wikipedia.org/wiki/List_of_SMTP_server_return_codes>

## SMB

<https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-cifs/8f11e0f3-d545-46cc-97e6-f00569e3e1bc>


## Timestamp

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
