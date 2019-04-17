#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Main Command Line Interface for Plugin Management
"""
import click
import os
from pkg_resources import iter_entry_points
from click_plugins import with_plugins
from .model import Message
from .core import TemplateManager
from jinja2 import Environment, PackageLoader, select_autoescape
env = Environment(
    loader=PackageLoader('apeiron', 'resources/templates', encoding='utf-8'),
    autoescape=select_autoescape(['html', 'xml'])
)

def get_env_vars(ctx, args, incomplete):
    return [k for k in os.environ.keys() if incomplete in k]


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
@click.argument("name", autocompletion=get_env_vars)
def create(name):
    tm = TemplateManager()
    print(tm.fill('report.html'))


@click.command()
@click.argument("color", type=click.STRING)
def cmd(color):
    Message.info('info message')
    Message.sucess('success message')
    Message.error('error message')
    Message.warning('warning message')


cli.add_command(create)
cli.add_command(cmd)
