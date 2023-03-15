# Speed

## Latency Table

| Medium                             | nanoseconds      | milliseconds |
|------------------------------------|------------------|--------------|
| L1 cache reference                 | 0.5 ns           |              |
| Branch mispredict                  | 5   ns           |              |
| L2 cache reference                 | 7   ns           |              |
| Mutex lock/unlock                  | 25   ns          |              |
| Main memory reference              | 100   ns         |              |
| Compress 1K bytes with Zippy       | 3,000   ns       |              |
| Send 1K bytes over 1 Gbps network  | 10,000   ns      | 0.01 ms      |
| Read 1 MB sequentially from memory | 250,000   ns     | 0.25 ms      |
| Round trip within same datacenter  | 500,000   ns     | 0.5  ms      |  
| Read 1 MB sequentially from SSD    | 1,000,000   ns   | 1    ms      |
| Disk seek                          | 10,000,000   ns  | 10    ms     |
| Read 1 MB sequentially from disk   | 20,000,000   ns  | 20    ms     |
| Send packet CA → Netherlands → CA    | 150,000,000   ns | 150    ms    |

## Mobile internet download speeds

| Gen | Short |     Technology     | Max Download Speed | AVG Download Speed |
|:---:|:-----:|:------------------:|:------------------:|:------------------:|
| 2G  |   G   |        GPRS        |     0.1Mbit/s      |     <0.1Mbit/s     |
| 2G  |   E   |        EDGE        |     0.3Mbit/s      |     0.1Mbit/s      |
| 3G  |  3G   |     3G (Basic)     |     0.3Mbit/s      |     0.1Mbit/s      |
| 3G  |   H   |        HSPA        |     7.2Mbit/s      |     1.5Mbit/s      |
| 3G  |  H+   |       HSPA+        |      21Mbit/s      |      4Mbit/s       |
| 3G  |  H+   |      DC-HSPA+      |      42Mbit/s      |      8Mbit/s       |
| 4G  |  4G   |   LTE Category 4   |     150Mbit/s      |      15Mbit/s      |
| 4G+ |  4G+  | LTE-Advanced Cat6  |     300Mbit/s      |      30Mbit/s      |
| 4G+ |  4G+  | LTE-Advanced Cat9  |     450Mbit/s      |      45Mbit/s      |
| 4G+ |  4G+  | LTE-Advanced Cat12 |     600Mbit/s      |      60Mbit/s      |
| 4G+ |  4G+  | LTE-Advanced Cat16 |     979Mbit/s      |      90Mbit/s      |
| 5G  |  5G   |         5G         | 1,000-10,000Mbit/s |   150-200Mbit/s    |
