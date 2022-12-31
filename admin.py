#!venv/bin/python
import click
import os
import ssh_connect


@click.group(invoke_without_command=False)
@click.pass_context
def adm(ctx):
    pass

@adm.command()
def show():
    files = [f for f in os.listdir('.') if f[-3::] in ['.py', '.sh']]
    files.remove('admin.py')
    click.echo('[Available Scripts]')
    for i, file in enumerate(files):
        click.echo(f'({i+1}) {file}')

if __name__ == '__main__':
    adm()
