# External Libraries
import click

# Internal Libraries
from .schemas import orm


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'],
                        max_content_width=80)


@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option()
def cli():
    pass


@cli.command('db')
def db():
    click.echo('db command')
