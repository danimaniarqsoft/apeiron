#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Main Command Line Interface for Plugin Management
"""
import os
import click
from pkg_resources import iter_entry_points
from click_plugins import with_plugins
from .commons import Message
from .core import TemplateManager

@with_plugins(iter_entry_points('apeirion.plugins'))
@click.group()
def cli():
    """
    This is the default CLI command.
    \b
        For add new plugins, please read the documentation
    \b
    """


@cli.command()
@click.argument("name")
def create(name):
    model =	{
        "name": "Ford",
        "body": "Mustang"
    }
    print(TemplateManager.fill('report.html', model))

@cli.command()
@click.option('--email', prompt='Email')
def metadata(email):
    model = {"email": email}
    print(TemplateManager.fill('CONTRIBUTING.md', model))
