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
from apeiron.commands.add_command_operations import AddCommandOperations
from apeiron.commons.help_messages import HelpMessages

from pathlib import Path


@click.group(help='Command to  add <components>')
def add():
    pass


@add.command()
@click.option('--email', default="none@noe.com", prompt='Email',
              help="Add a Contributing File")
@click.option('--force', '-f', is_flag=True)
def contributing_file(email, force):
    if AddCommandOperations.add(email, force):
        Message.sucess("Contributing file was added!")
    else:
        Message.failure("Conflict must be resolved")
