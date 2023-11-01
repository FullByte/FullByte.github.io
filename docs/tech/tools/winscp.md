# WinSCP

| What          | Where                |
|---------------|----------------------|
| Official Page | <https://winscp.net> |

## Script Examples

If you want to automate data transfers using WinSCP, you can use scripting.

### Basic Example

Here's a basic example of how you can write a script to transfer files:

Create a text file (e.g., myscript.txt) with the following content:

```bash
# Automatically answer all prompts negatively not to stall
# the script on errors
option batch on
# Disable overwrite confirmations that conflict with the previous
option confirm off
# Connect using a stored session (replace 'MySession' with your session name)
open MySession
# Change remote directory
cd /path/to/remote/directory
# Force binary mode transfer
option transfer binary
# Download file to the local directory
get remote-file.txt C:\local\path\
# Disconnect
close
# Exit WinSCP
exit
```

Use the WinSCP command-line interface to run the script:

```bash
winscp.com /script=path\to\myscript.txt
```

Logging:
You can add ```/log=path\to\log.log``` to create a log of the transfer, which can be useful for debugging.

### Uploading Files with a Specific Extension

If you want to upload only .txt files from a local directory to a remote directory:

```bash
option batch on
option confirm off
open MySession
lcd C:\local\path
cd /remote/path
put *.txt
close
exit
```

### Synchronizing Directories

To synchronize a local directory with a remote directory (uploads new and updated files):

```bash
option batch on
option confirm off
open MySession
lcd C:\local\path
cd /remote/path
synchronize remote -criteria=size C:\local\path /remote/path
close
exit
```

### Handling Errors

To handle errors and continue with the script execution:

```bash
option batch continue
option confirm off
open MySession
# Try to download a file. If it fails, the script continues.
get /remote/path/nonexistent.txt C:\local\path\
# This will be executed even if the previous command fails.
get /remote/path/existent.txt C:\local\path\
close
exit
```

### Conditional File Transfer

Transfer files only if a specific "flag" file exists:

```bash
option batch on
option confirm off
open MySession
# Check if flag file exists
stat /remote/path/flag.txt
if $? == 0
    get /remote/path/data.txt C:\local\path\
end
close
exit
```

### Automating with Passwords

While it's not recommended to include passwords in scripts (due to security concerns), it's possible:

```bash
option batch on
option confirm off
# Use the -passive=on option if you're behind a firewall.
open ftp://username:password@ftp.example.com -passive=on
lcd C:\local\path
cd /remote/path
put uploadfile.txt
close
exit
```

### Deleting Files After Successful Transfer

To delete local files after a successful upload:

```bash
option batch on
option confirm off
open MySession
lcd C:\local\path
cd /remote/path
put -delete *.txt
close
exit
```
