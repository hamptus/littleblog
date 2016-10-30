import os
import click

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

    template_dir = os.path.join(project_name, 'templates')
    
    os.makedirs(template_dir)

    os.makedirs(os.path.join(project_name, 'posts'))
 
    with open(os.path.join(project_name, 'settings.py'), 'w') as settings:
        settings.write('#!/usr/bin/env python3\n')

    open(os.path.join(template_dir, 'base.html'), 'w').close()


    for fn in ('detail.html', 'list.html'):
        with open(os.path.join(template_dir, fn), 'w') as f:
            f.write("{% extends 'base.html' %}")
            
    click.echo("Created {}".format(project_name))


cli.add_command(start)


if __name__ == '__main__':
    cli()
