import paramiko
import socket
import traceback

__author__ = 'Birender'

# Paramiko is a Python (2.7, 3.4+) implementation of the SSHv2 protocol [1], providing both client and server functionality. While it leverages a Python C extension for low level cryptography (Cryptography), Paramiko itself is a pure Python interface around SSH networking concepts.

def validate_ssh_output(cmd_status, output, msg):
    if cmd_status != 0:
        print("command fails")
        raise Exception(output)
    else:
        print("Command success:" + msg )

class SshInfo():
    def __init__(self, host, user, password, port = 22, timeout=60):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.timeout = timeout

class Ssh:
    client = None

    def __init__(self, ssh_info):
        self.sshinfo = ssh_info

    def ssh_command(self, command, log_level='info'):

        print("Executing SSH on %s:%d: %s" % (self.sshinfo.host, self.sshinfo.port, command))

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        def float_or_null(val):
            return float(val) if val else val

        try:
            ssh.connect(self.sshinfo.host,
                        port=self.sshinfo.port,
                        username=self.sshinfo.user,
                        password=self.sshinfo.password,
                        timeout=float_or_null(self.sshinfo.timeout),
                        banner_timeout=float_or_null(self.sshinfo.timeout))
        except (socket.error, socket.gaierror, paramiko.ssh_exception.SSHException) as e:
            if "Error reading SSH protocol banner" in str(e):
                raise Exception(f'Error {e}, try longer ssh_timeout for {self.sshinfo.host}')
            else:
                raise Exception(f'Error {e}, when connecting to {self.sshinfo.host}')

        transport = ssh.get_transport()
        channel = transport.open_session()
        channel.set_combine_stderr(True)
        channel.exec_command(command)
        stdout = channel.makefile()

        def dummy(text):
            pass

        def stdout_readline():
            try:
                return stdout.readline(2048)
            except UnicodeDecodeError as e:
                return "line generated exception"

        output = ""
        for line in iter(stdout_readline(),""):
            output += line

        cmd_status = channel.recv_exit_status()
        ssh.close()
        print("SSH cmd_status:" + str(cmd_status))

        return cmd_status, output

