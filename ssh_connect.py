#!/usr/bin/python3
import select
import socket
import sys
import termios
import tty
from paramiko.py3compat import u
from paramiko.client import SSHClient, AutoAddPolicy


# ------------------------- User Defined Variables -------------------------- #

SSH_USER = "vagrant"
SSH_HOST = "192.168.56.111"
SSH_PORT = 22
SSH_KEY  = 'vagrant/vg_box'

# ------------------------- User Defined Variables -------------------------- #


class SSHConnect():
    def __init__(self, user, host, port, key):
        self.ssh_user = user
        self.ssh_host = host
        self.ssh_port = port
        self.ssh_key  = key

    def _connect(self):
        self.client = SSHClient()
        self.client.set_missing_host_key_policy(AutoAddPolicy())
        self.client.load_system_host_keys()
        self.client.connect(SSH_HOST, port=SSH_PORT,
                                 username=SSH_USER,
                                 key_filename=SSH_KEY)

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
    sc = SSHConnect(SSH_USER, SSH_HOST, SSH_PORT, SSH_KEY)
    sc.cmd('df -h /')
