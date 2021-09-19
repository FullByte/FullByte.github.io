# PEASS

<https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite>

## Linpeas

Download linpeas and copy it target e.g. 10.10.112.131

```sh
wget https://raw.githubusercontent.com/carlospolop/privilege-escalation-awesome-scripts-suite/master/linPEAS/linpeas.sh
scp linpeas.sh user@10.10.112.131:/dev/shm
chmod +x linpeas.sh
./linpeas.sh
```
