#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Main Command Line Interface for Plugin Management
"""
import os
import click
from pkg_resources import iter_entry_points
from click_plugins import with_plugins
from apeiron.commons import Message, Files
from apeiron.core import TemplateManager

from pathlib import Path


@with_plugins(iter_entry_points('apeirion.plugins'))
@click.group()
def cli():
    pass

@cli.command()
@click.option('--email', default="none@noe.com", prompt='Email')
def add_contributing_file(email):
    model = {"email": email}
    text = TemplateManager.fill('CONTRIBUTING.md', model)
    file_path = Files.save(text, 'CONSTRIBUTING_borrar.md')
    if file_path is not None:
        Message.info('Saving file to : '+file_path.as_posix())
    else:
        Message.error('File exist')

@cli.command()
def test():
    file_data = Path(os.getcwd())
    file_data = file_data / "hola.txt"
    result = Files.save("holas.txt", "Saludos a todos")
    print(result.as_posix())