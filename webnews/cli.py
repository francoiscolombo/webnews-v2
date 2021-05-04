import click
import os


@click.group()
def cli():
    ...


@click.command(name='start')
def start():
    os.system('uvicorn webnews.app:app --reload')


cli.add_command(start)
