# CMD

## Robocopy

exclude files

```cmd
Robocopy /xd excludethis
```

Ignore hidden files

```cmd
Robocopy -s -h
```


## Format and Image stuff

### Format FAT32 on >32GB

use diskpart to clean the disk (as Admin)

```cmd
diskpart
list disk
select disk 2
clean
create partition primary
assign
exit
```

use h2format to format the disk (64kb clusters) e.g. for drive x:

```cmd
h2format x: 64
```
