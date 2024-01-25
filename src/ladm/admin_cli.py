#!venv/bin/python
import click
import os
import json
from ladm import ssh_connect, systemd

full_path = os.path.dirname(__file__)
shell_dir = f"{full_path}/bash"


@click.group(invoke_without_command=False)
@click.pass_context
def adm(empty):
    pass


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
    os.system(f"{shell_dir}/find_ip_info.sh {ip}")


@adm.command()
@click.option("-t", "--title", required=True)
@click.option("-n", "--length", type=int)
def separator(title, length):
    if not length:
        length = ""
    os.system(f"{shell_dir}/separator.sh {title} {length}")


@adm.command()
@click.option("-p", "--path", required=True, type=str)
@click.option("-e", "--exclude", required=False, type=str)
def sensfind(path, exclude):
    if not exclude:
        exclude = ""
    os.system(f"{shell_dir}/find_sensitive_info.sh {path} {exclude}")


@adm.command()
@click.option("-s", "--service", is_flag=True)
@click.option("-t", "--timer", is_flag=True)
@click.option("-f", "--filename", type=str)
@click.option("-v", "--vars")
def sysd(service, timer, filename, vars):
    vars = json.loads(vars)
    template = None
    if service:
        template = "service.j2"
    elif timer:
        template = "timer.j2"
    systemd.create_config(filename, template, vars)
    systemd.reload()


@adm.command()
@click.option("-z", "--zone", type=str)
def fwdsource(zone):
    if not zone:
        zone = ""
    os.system(f"{shell_dir}/get_fw_sources.sh {zone}")


@adm.command()
@click.option("-r", "--run", type=str)
@click.option("-s", "--show", is_flag=True)
def bash(run, show):
    if show:
        files = [f for f in os.listdir(shell_dir)]
        click.echo("[Bash Scripts]")
        for i, file in enumerate(files):
            click.echo(f"({i+1}) {file}")
    elif run:
        run = run.split(" ")
        cmd = run[0]
        if len(run) == 1:
            os.system(f"{shell_dir}/{cmd}")
        else:
            params = " ".join(run[1:])
            os.system(f"{shell_dir}/{cmd} {params}")

    else:
        print("Please choose an action: --show or --run <script>")


if __name__ == "__main__":
    adm()
