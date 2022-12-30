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
    def __init__(self, cred_name, host):
        self.host = host
        self.port = 22
        self.cred = self.find_env_cred(cred_name)

    def find_env_cred(self, cred_name):
        i = 1
        while True:
            name = os.getenv(f'sc_name_{i}')
            user = os.getenv(f'sc_user_{i}')
            key  = os.getenv(f'sc_key_{i}')
            if user or key:
                i += 1
                if name == cred_name:
                    return (user, key)
            else:
                print('Credentials were not found')
                sys.exit(0)

    def _connect(self):
        self.client = SSHClient()
        self.client.set_missing_host_key_policy(AutoAddPolicy())
        self.client.load_system_host_keys()
        self.client.connect(self.host, port=self.port,
                            username=self.cred[0], key_filename=self.cred[1])

    def _interactive(self, chan):
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
        self._connect()
        try:
            channel = self.client.get_transport().open_session()
            channel.get_pty()
            channel.invoke_shell()
            self._interactive(channel)
            self.client.close()
        except Exception:
            print("Failed")

    def cmd(self, cmd):
        self._connect()
        stdin, stdout, stderr = self.client.exec_command(cmd)
        for line in stdout.readlines():
            print(line.replace('\n', ''))
        for line in stderr.readlines():
            print(line.replace('\n', ''))
        self.client.close()


if __name__ == '__main__':
    cred_name = sys.argv[1]
    host = sys.argv[2]
    sc = SSHConnect(cred_name, host)
    sc.cmd('df -h /')
