from paramiko import SSHClient
from scp import SCPClient

client = SSHClient()
client.load_host_keys("/Users/vincentzhao/.ssh/known_hosts")
client.load_system_host_keys()

hostname = "gilbreth.rcac.purdue.edu"
username = "zhao1322"

client.connect(hostname, username=username)

def progress(filename, size, sent):
    print("%s\'s progress: %.2f%%   \r" % (filename, float(sent)/float(size)*100) )

scp = SCPClient(client.get_transport(), progress=progress)

def execute_cmd(cmd):
    stdin, stdout, stderr = client.exec_command(cmd)
    output = stdout.read().decode("utf8")
    print("EXECUTING:", cmd)
    print(f'STDOUT: {output}')
    print(f'STDERR: {stderr.read().decode("utf8")}')
        
    print(f"Return code: {stdout.channel.recv_exit_status()}")
    
    stdin.close()
    stdout.close()
    stderr.close()
    
    return output

def queue_project(project_folder, dependency=""):

    project_path = '/home/zhao1322/test/' + project_folder

    # scp.put(project_folder, recursive=True, remote_path='/home/zhao1322/test')

    scp.put("job.sh", remote_path=project_path)
    scp.put("cleanup.sh", remote_path=project_path)
    # scp.put("scoring.sh", remote_path=project_path)

    print("Queuing SLURM Job")
    if dependency:
        out = execute_cmd(f'cd {project_path}; sbatch --dependency=afterany:{dependency} job.sh')
    else:
        out = execute_cmd(f'cd {project_path}; sbatch job.sh')
    
    slurm_id = out.split(" ")[-1].strip()
    
    print("Queuing scoring")
    
    out = execute_cmd(f'cd /home/zhao1322/test; sbatch --dependency=afterany:{slurm_id} scoring.sh')
    
    slurm_id = out.split(" ")[-1].strip()
    
    print("Queuing cleanup")
    out = execute_cmd(f'cd {project_path}; sbatch --dependency=afterany:{slurm_id} cleanup.sh')
    
    slurm_id = out.split(" ")[-1].strip()
    print("slurm id", slurm_id)
    
    return slurm_id
queue_project('example_submission-mt3')
print("project queued")
scp.close()
client.close()