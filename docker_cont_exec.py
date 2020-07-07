import sys
try :
   import docker,argparse
except :
   print("EXCEPTION :( Please install the docker and argparse libraries")
   sys.exit(1)
from argparse import RawTextHelpFormatter

parser = argparse.ArgumentParser(description = "Docker Container Command Exec\nThis script runs a command on every container running in the list of IPs provided which have the Docker API exposed.\n- github.com/notnotnotveg", formatter_class=RawTextHelpFormatter )
parser.add_argument("-p", "--port", help="Set port (default: 2375)")
parser.add_argument("-c", "--cmd", help="Command to be executed (default: whoami)")

requiredNamed = parser.add_argument_group('required named arguments')
requiredNamed.add_argument("-i", "--ip_file", help="File with new line seperated IPs", required=True)

args = parser.parse_args()

arg_port = "2375"
arg_cmd = "whoami"


if args.port:
    arg_port = args.port

if args.cmd:
    arg_cmd = args.cmd

open_file= open(args.ip_file)
for LINE in iter(open_file):
    ip = LINE.rstrip()
    url = 'tcp://' + ip + ':' + arg_port;
    client = docker.DockerClient(base_url= url)
    print("Host : " + ip + ":" + arg_port)
    try:
        for container in client.containers.list():
            print("Container Name : " + container.name)
            print("Container Image : " + str(container.image).split("'")[1])
            print("Output of " + arg_cmd + ":")
            try :
                print(container.exec_run(arg_cmd).output.decode('utf-8'))
            except :
                print("EXCEPTION :( Cannot run command on container")
    except:
        print("EXCEPTION :( Cannot connect to host")
    print("###################################################")

