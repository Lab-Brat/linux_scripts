#!venv/bin/python
import click
import os
import ssh_connect
import find_ip_info


@click.group(invoke_without_command=False)
@click.pass_context
def adm(empty):
    pass

@adm.command()
def show():
    files = [f for f in os.listdir('.') if f[-3::] in ['.py', '.sh']]
    files.remove('admin.py')
    click.echo('[Available Scripts]')
    for i, file in enumerate(files):
        click.echo(f'({i+1}) {file}')

@adm.command()
@click.option('-n', '--name', required=True, type=str)
@click.option('-h', '--host', required=True, type=str)
@click.option('-t', '--terminal', is_flag=True)
@click.option('-c', '--command', type=str)
def ssh(name, host, terminal, command):
    sc = ssh_connect.SSHConnect(name, host)
    if terminal:
        sc.terminal()
    elif command:
        sc.cmd(command)

@adm.command()
@click.option('-i', '--ips', required=True, type=str)
def ipfind(ips):
    for ip in ips.split(','):
        ip_info  = find_ip_info.get_info_local(ip)
        find_ip_info.pretty_print(ip_info)

if __name__ == '__main__':
    adm()
