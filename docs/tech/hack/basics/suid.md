# SUID

| Permission | On Files                                                      | On Directories                                           |
|------------|---------------------------------------------------------------|----------------------------------------------------------|
| SUID Bit   | User executes the file with permissions of the file owner     | -                                                        |
| SGID Bit   | User executes the file with the permission of the group owner | File created in directory gets the same group owner      |
| Sticky Bit | No meaning                                                    | Users are prevented from deleting files from other users |

SUID bits can be dangerous, some binaries such as passwd need to be run with elevated privileges (as its resetting your password on the system), however other custom files could that have the SUID bit can lead to all sorts of issues.

To search the a system for these type of files run the following:

```find / -perm -u=s -type f 2>/dev/null```
