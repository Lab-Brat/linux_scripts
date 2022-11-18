#!venv/bin/python
import click
import os

@click.command()
def show():
    files = [f for f in os.listdir('.') if f[-3::] in ['.py', '.sh']]
    files.remove('admin.py')
    click.echo('[Available Scripts]')
    for i, file in enumerate(files):
        click.echo(f'({i+1}) {file}')
    click.echo('\n')

if __name__ == '__main__':
    show()
