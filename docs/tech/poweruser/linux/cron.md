# Cron

## Examples

```shell
Every Minute    * * * * *
Every Five Minutes    */5 * * * *
Every 10 Minutes    */10 * * * *
Every 15 Minutes    */15 * * * *
Every 30 Minutes    */30 * * * *
Every Hour    0 * * * *
Every Two Hours    0 */2 * * *
Every Six Hours    0 */6 * * *
Every 12 Hours    0 */12 * * *
During the Work Day    */5 9-17 * * *
Every day at Midnight    0 0 * * *
Every Two Weeks    0 0 * * Sun [ $(expr $(date +%W) % 2) -eq 1 ] && /path/to/command
At the Start of Every Month    0 0 1 * *
On January 1st at Midnight    0 0 1 1 *
```
