import paramiko
import socket

def run_command(host, port, username, password, command):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ssh.connect(host, port=port, username=username, password=password, timeout=5)

        stdin, stdout, stderr = ssh.exec_command(command)

        output = stdout.read().decode()
        error = stderr.read().decode()

        ssh.close()

        return output if output else error

    except paramiko.AuthenticationException:
        return "ERROR: Authentication Failed"

    except socket.timeout:
        return "ERROR: Connection Timeout"

    except Exception as e:
        return f"ERROR: {str(e)}"