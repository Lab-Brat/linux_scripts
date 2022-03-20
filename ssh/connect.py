#!/usr/bin/python3
import getpass
from paramiko.client import SSHClient, AutoAddPolicy

SSH_USER = "root"
SSH_HOST = "rocky1.loc.vm"
SSH_PORT = 22
SSH_PASS = getpass.getpass(prompt=f'Password for {SSH_HOST}: ')

client = SSHClient()
client.set_missing_host_key_policy(AutoAddPolicy())

client.load_system_host_keys()
try:
    client.connect(SSH_HOST, port=SSH_PORT,
                             username=SSH_USER,
                             password=SSH_PASS,
                             look_for_keys=False)
    print("Connected Successfully")
except Exception:
    print("Failed to establish connection")

finally:
    client.close()

