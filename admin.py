#!venv/bin/python
import click
import os

@click.command()
def show():
    files = [f for f in os.listdir('.') if f[-2::] in ['py', 'sh']]
    click.echo(files)

if __name__ == '__main__':
    show()
