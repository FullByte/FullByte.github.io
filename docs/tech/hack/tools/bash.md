# Bash

## SUID bits

SUID bits can be dangerous, some binaries such as passwd need to be run with elevated privileges (as its resetting your password on the system), however other custom files could that have the SUID bit can lead to all sorts of issues. To search a system for these type of files run the following:

 ```sh
find / -perm -u=s -type f 2>/dev/null
```

## Get a TTY Shell

If you get shell without TTY, here are some commands you can try to fix this.

Choose an option based on the what is installed on the system:

- Bash ```echo os.system('/bin/bash')``` or ```/bin/sh -i```
- Python: ```python -c 'import pty; pty.spawn("/bin/sh")'```
- Perl: ```perl —e 'exec "/bin/sh";'``` or ```perl: exec "/bin/sh";```
- Lua: ```lua: os.execute('/bin/sh')```
- Ruby: ```ruby: exec "/bin/sh"``` or from within Interactive Ruby Shell ```exec "/bin/sh"```
- Vi from within vi ```:!bash``` or  ```:set shell=/bin/bash:shell```
- nmap interactive mode: ```!sh```
