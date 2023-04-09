#!venv/bin/python
import click
import os
import json
import create_boundary
import find_sensinfo
import ssh_connect
import systemd


@click.group(invoke_without_command=False)
@click.pass_context
def adm(empty):
    pass


@adm.command()
@click.option("-b", "--bash", is_flag=True)
def show(bash):
    tp = ("./bash", ".sh") if bash else (".", ".py")
    files = [f for f in os.listdir(tp[0]) if f[-3::] == tp[1] and f != "admin.py"]
    click.echo("[Available Scripts]")
    for i, file in enumerate(files):
        click.echo(f"({i+1}) {file}")


@adm.command()
@click.option("-h", "--host", required=True, type=str)
@click.option("-k", "--add-key", is_flag=True)
@click.option("-c", "--command", type=str)
def ssh(host, add_key, command):
    sc = ssh_connect.SSHConnect(host)
    if command:
        sc.cmd(command)
    elif add_key:
        sc.add_key()


@adm.command()
@click.option("-i", "--ip", required=True, type=str)
def ipfind(ip):
    os.system(f"bash/find_ip_info.sh {ip}")


@adm.command()
@click.option("-t", "--title", required=True)
@click.option("-n", "--length", type=int)
def separator(title, length):
    create_boundary.get_boundary(title, length)


@adm.command()
@click.option("-p", "--path", required=True, type=str)
@click.option("-e", "--exclude", required=False, type=str)
def sensfind(path, exclude):
    find_sensinfo.find_info(path, exclude)


@adm.command()
@click.option("-s", "--service", is_flag=True)
@click.option("-t", "--timer", is_flag=True)
@click.option("-f", "--filename", type=str)
@click.option("-v", "--vars")
def sysd(service, timer, filename, vars):
    vars = json.loads(vars)
    if service:
        template = "service.j2"
    elif timer:
        template = "timer.j2"
    systemd.create_config(filename, template, vars)
    systemd.reload()


@adm.command()
@click.option("-r", "--run", type=str)
def bash(run):
    full_path = os.path.dirname(__file__)
    os.system(f"{full_path}/bash/{run}.sh")


if __name__ == "__main__":
    adm()
