#!/usr/bin/python3
import select
import socket
import sys
import os
import termios
import tty
from paramiko.py3compat import u
from paramiko.client import SSHClient, AutoAddPolicy


class SSHConnect():
    def __init__(self, host):
        self.host = host
        self.port = 22
        self.cred = self.find_env_cred()

    def find_env_cred(self):
        '''
        Read available credentials and find the specified one.
        '''
        cred_name = os.getenv('ADMIN_SSH_CRED')
        i = 1
        while True:
            name = os.getenv(f'sc_name_{i}')
            user = os.getenv(f'sc_user_{i}')
            key  = os.getenv(f'sc_key_{i}')
            pasw = os.getenv(f'sc_pas_{i}')
            if user or key:
                i += 1
                if name == cred_name:
                    return (user, key, pasw)
            else:
                print('Credentials were not found')
                sys.exit(0)

    def _connect(self, auth_method):
        '''
        Establish a SSH connection.
        '''
        print(self.cred)
        self.client = SSHClient()
        self.client.set_missing_host_key_policy(AutoAddPolicy())
        self.client.load_system_host_keys()
        if auth_method == 'key':
            self.client.connect(self.host,
                port=self.port,
                username=self.cred[0], key_filename=self.cred[1])
        elif auth_method == 'password':
            self.client.connect(self.host,
                port=self.port,
                username=self.cred[0], password=self.cred[2],
                allow_agent=False, look_for_keys=False)
        else:
            print('Unknown Authentication Method')

    def _show_output(self, stdout, stderr):
        '''
        Show full output of both stdout and stderr
        of the command that was ran on the host.
        '''
        for line in stdout.readlines():
            print(line.replace('\n', ''))
        for line in stderr.readlines():
            print(line.replace('\n', ''))

    def cmd(self, cmd):
        '''
        Run a single command supplied by the user.
        '''
        self._connect(auth_method='key')
        _, stdout, stderr = self.client.exec_command(cmd)
        self._show_output(stdout, stderr)
        self.client.close()

    def _read_key(self):
        '''
        Read public key file from the environmental variable.
        '''
        with open(f'{self.cred[1]}.pub', 'r') as key_file:
            return key_file.readlines()[0]

    def _create_ssh_directory(self):
        '''
        Create users' default SSH configuration repository 
        if it doesn't exist.
        '''
        _, _, stderr = self.client.exec_command('ls -l ~/.ssh')
        if "No such file" in str(stderr.readlines()):
            self.client.exec_command('mkdir ~/.ssh')
            print('SSH directory created')

    def add_key(self):
        '''
        Add user's public SSH key to authorized_keys files.
        '''
        key_content = self._read_key()
        self._connect(auth_method='password')
        self._create_ssh_directory()

        cmd = f'echo "{key_content}" >> ~/.ssh/authorized_keys'
        stdin, stdout, stderr = self.client.exec_command(cmd)
        self._show_output(stdout, stderr)
        if stderr.readlines() == []:
            print('Key Added!')
        self.client.close()

    def _interactive(self, chan):
        '''
        [ DEPRECARED ]
        Launch an interactive Terminal.
        '''
        oldtty = termios.tcgetattr(sys.stdin)
        try:
            tty.setraw(sys.stdin.fileno())
            tty.setcbreak(sys.stdin.fileno())
            chan.settimeout(0.0)

            while True:
                r, w, e = select.select([chan, sys.stdin], [], [])
                if chan in r:
                    try:
                        x = u(chan.recv(1024))
                        if len(x) == 0:
                            sys.stdout.write("\r\n*** EOF\r\n")
                            break
                        sys.stdout.write(x)
                        sys.stdout.flush()
                    except socket.timeout:
                        pass
                if sys.stdin in r:
                    x = sys.stdin.read(1)
                    if len(x) == 0:
                        break
                    chan.send(x)
        finally:
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, oldtty)

    def terminal(self):
        '''
        [ DEPRECARED ]
        Connect with an interactive Terminal.
        '''
        self._connect()
        try:
            channel = self.client.get_transport().open_session()
            channel.get_pty()
            channel.invoke_shell()
            self._interactive(channel)
            self.client.close()
        except Exception:
            print("Failed")


if __name__ == '__main__':
    cred_name = sys.argv[1]
    host = sys.argv[2]
    sc = SSHConnect(cred_name, host)
    sc.cmd('df -h /')
