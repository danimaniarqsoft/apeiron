#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Main Command Line Interface for Plugin Management
"""
import os
import click
from pkg_resources import iter_entry_points
from click_plugins import with_plugins
from apeiron.commons import Message, Files, FileVersionManager
from apeiron.core import TemplateManager
from apeiron.commands.add import add

from pathlib import Path

@with_plugins(iter_entry_points('apeirion.plugins'))
@click.group()
def cli():
    pass

cli.add_command(add)

def sni_message(*datas):
    print('-'.join(datas))

if __name__ == "__main__":
    click.echo(click.style('Hello World!', fg='green')+click.style('Hello World!', fg='red'))
