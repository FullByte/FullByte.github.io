# Get a TTY Shell

If you get shell without TTY, here are some commands you can try to fix this.

Choose an option based on the what is installed on the system:

- Bash ```echo os.system('/bin/bash')``` or ```/bin/sh -i```
- Python: ```python -c 'import pty; pty.spawn("/bin/sh")'```
- Perl: ```perl —e 'exec "/bin/sh";'``` or ```perl: exec "/bin/sh";```
- Lua: ```lua: os.execute('/bin/sh')```
- Ruby: ```ruby: exec "/bin/sh"``` or from within Interactive Ruby Shell ```exec "/bin/sh"```
- Vi from within vi ```:!bash``` or  ```:set shell=/bin/bash:shell```
- nmap interactive mode: ```!sh```
