#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Main Command Line Interface for Plugin Management
"""
import os
import click
import difflib
from pkg_resources import iter_entry_points
from click_plugins import with_plugins
from apeiron.commons import Message, Files, FileVersionManager
from apeiron.core import TemplateManager
from apeiron.commands.add_command_operations import AddCommandOperations
from apeiron.commons.help_messages import HelpMessages

from pathlib import Path
import glob

@click.group(help='Command to  add <components>')
def show():
    pass


@show.command()
@click.option('--file')
def conflicts(file):
    if not file:
        files_finded = glob.iglob('**/*.conflict', recursive=True)
        count = 0
        for file in files_finded:
            Message.failure(Path(file).with_suffix('').as_posix())
            count = count + 1
        Message.failure('Conflicts founded:', str(count))
    else:
        left_file_path = Path(file)
        right_file_path = Path(left_file_path.parent / (left_file_path.name + '.conflict'))
        FileVersionManager.diff(Path(file), Path(right_file_path))
