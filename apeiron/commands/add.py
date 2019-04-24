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

from pathlib import Path

@click.group()
def add():
    pass

@add.command()
@click.option('--email', default="none@noe.com", prompt='Email')
def contributing_file(email):
    if AddCommandOperations.add(email):
        Message.sucess("contributing file was added!")
    else:
        Message.error("Conflict must be resolved before")

@add.command()
def test():
    file_data = Path(os.getcwd())
    file_data = file_data / "LICENSE"
    print(FileVersionManager.hash(file_data))
