import os
import importlib.util

from jinja2 import Environment, FileSystemLoader


env = Environment(loader=FileSystemLoader('templates'))


def load_settings(project_name):
    """ Load the settings.py file from the specified project_name directory """
    spec = importlib.util.spec_from_file_location('settings', os.path.join(project_name, 'settings.py'))
    settings = importlib.util.module_from_spec(spec)
    
    try:
        spec.loader.exec_module(settings)
    except FileNotFoundError:
        return
  
    return settings


