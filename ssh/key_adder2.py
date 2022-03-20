#!/usr/bin/python3
import os

#============================ start of user defined variables ==============================

host_list = ['ucs-frontend-1.loc.vm', 'ucs-frontend-2.loc.vm',
             'ucs-mail-1.loc.vm', 'ucs-mail-2.loc.vm',
             'ucs-apps-1.loc.vm', 'ucs-apps-2.loc.vm',
             'ucs-extra-1.loc.vm', 'ucs-extra-2.loc.vm',
             'ucs-dos-1.loc.vm', 'ucs-dos-2.loc.vm', 'ucs-dos-3.loc.vm',
             'ucs-db-1.loc.vm', 'ucs-db-2.loc.vm', 'ucs-db-3.loc.vm',
             'ucs-infra-1.loc.vm']
subnet = '192.168.8.'
ip_range = [1, 15]
ssh_pass = 'password'

#============================= end of user defined variables ===============================


class add_key():
    def __init__(self, host_list):
        self.hl = host_list
        self.subnet = subnet
        self.ip_range = ip_range
        self.spass = ssh_pass
        self.keys_path = '/root/.ssh/'
        self.conf_file = f'{self.keys_path}/config'

    def add_conf(self, i, hn):
        os.system(f"echo 'Host {hn}' >> {self.conf_file}")
        os.system(f"echo '        User root' >> {self.conf_file}")
        os.system(f"echo '        Port 22' >> {self.conf_file}")
        os.system(f"echo '        IdentityFile ~/.ssh/ucs_hn_{i}' >> {self.conf_file}")
        os.system(f"echo '' >> {self.conf_file}")

    def add(self):
        for i in range(ip_range[0], ip_range[1]+1):
            hn = self.hl[i-4]
            #os.system(f"echo '{self.subnet}{i} {hn}' >> /etc/hosts")
            os.system(f"ssh-keygen -f {self.keys_path}ucs_hn_{i} -P '' -q")
            os.system(f"sshpass -p '{self.spass}' ssh-copy-id -o StrictHostKeyChecking=no -i {self.keys_path}ucs_hn_{i} root@{hn}")
            self.add_conf(i, hn)

if __name__ == '__main__':
    ak = add_key(host_list)
    ak.add()

