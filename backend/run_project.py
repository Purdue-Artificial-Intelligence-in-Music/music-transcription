from paramiko import SSHClient
from scp import SCPClient
import time

client = SSHClient()
client.load_host_keys("/Users/vincentzhao/.ssh/known_hosts")
client.load_system_host_keys()

hostname = "gilbreth.rcac.purdue.edu"
username = "zhao1322"

client.connect(hostname, username=username)

def progress(filename, size, sent):
    print("%s\'s progress: %.2f%%   \r" % (filename, float(sent)/float(size)*100) )

scp = SCPClient(client.get_transport(), progress=progress)

folder_name = 'example_submission-mt3'

project_path = '/home/zhao1322/test/' + folder_name

scp.put(folder_name, recursive=True, remote_path='/home/zhao1322/test')

scp.put("job.sh", remote_path=project_path)


def execute_cmd(cmd):
    stdin, stdout, stderr = client.exec_command(cmd)
    
    print(f'STDOUT: {stdout.read().decode("utf8")}')
    print(f'STDERR: {stderr.read().decode("utf8")}')

    print(f'Return code: {stdout.channel.recv_exit_status()}')

    stdin.close()
    stdout.close()
    stderr.close()

print("Running SLURM Job")
execute_cmd(f'cd {project_path}; sbatch --nodes=1 --gpus-per-node=1 -A standby job.sh')

scp.close()
client.close()