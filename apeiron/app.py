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


@click.command()
@cli.argument("name")
def create(name):
    model =	{
        "name": "Ford",
        "body": "Mustang"
    }
    print(TemplateManager.fill('report.html', model))

@click.command()
@cli.argument('email', required=True)
def metadata(email):
    model = {"email": email}
    print(TemplateManager.fill('CONTRIBUTING.md', model))
