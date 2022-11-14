# JSON Tools

``` txt
           `:+osyyyso+/:`
        :smNNNmmmddddhhhmds:
     .oNNNNNmmmddddhhhyyyymMNs.
    oNNNNNmmmddddhhhyyyyssshMMMs`
  .dNNNNmmmddmmmdyyyyysssooohMMMm.
 `mNNNmmmmmNMMMy-  .+ssoooo++NMMMN.
 yNNmmmdmMMMMN-      .ooo+++/dMMMMd
-NmmmddmMMMMM:        .+++///yMMMMM-
+mmddddMMMMMm          /////:yMMMMM+
+ddddhdMMMMMm          ///:::mMMMMM+
-ddhhhdMMMMMM-        `/::::yMMMMMM-
 shhyyhMMMMMMm-      `:::::hMMMMMMh
 .yyyyyNMMMMMMMs.  `-:::/yNMMMMMMm`
  .ossshMMMMMMMMMmhyyydNMMMMMMMMd.
    :ooodMMMMMMMMMMMMMMMMMMMMMNo
     `:++yNMMMMMMMMMMMMMMMMMNs.
        .-/ymMMMMMMMMMMMMmy:
            `-/oyhhhys+:`
```

## JQ

[jq](https://stedolan.github.io/jq/)

## JC

[jc](https://github.com/kellyjonbrazil/jc)

Example:

``` sh
dig 0xfab1.net | jc --dig | jq -r '.[].answer[].data'
```

Result:

``` txt
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153
```
