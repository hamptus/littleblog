import os
import shutil

import click
from . import little



_PARENT_DIR = os.path.abspath(os.path.dirname(__file__))
_SKEL_DIR = os.path.join(_PARENT_DIR, 'skel')
_SKEL_TEMPLATES = os.path.join(_SKEL_DIR, 'templates')


@click.group()
def cli():
    pass

@click.command()
@click.argument('project_name')
def start(project_name):
    try:
        os.mkdir(project_name)
    except FileExistsError:
        click.echo('The directory "{}" already exists. Remove or rename the existing "{}" directory or choose a different project name.'.format(project_name, project_name))
        return

    shutil.copyfile(os.path.join(_PARENT_DIR, 'skel', 'settings.py'), os.path.join(project_name, 'settings.py'))
    shutil.copytree(_SKEL_TEMPLATES, os.path.join(project_name, 'templates'))
    
    os.makedirs(os.path.join(project_name, 'posts'))

    click.echo("Created {}".format(project_name))


@click.command()
@click.argument('project_name')
def render(project_name):
    settings = little.load_settings(project_name)
    
    if not settings: 
        click.echo("Couldn't find settings.py in '{}'".format(project_name))
        return
cli.add_command(start)
cli.add_command(render)


if __name__ == '__main__':
    print(_PARENT_DIR)
    cli()
