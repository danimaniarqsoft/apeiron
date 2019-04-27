#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Main Command Line Interface for Plugin Management
"""
import os
import click
from pkg_resources import iter_entry_points
from click_plugins import with_plugins
from apeiron.commons import Message, Files, FileVersionManager, Apeiron
from apeiron.core import TemplateManager
from apeiron.commands.add_command_operations import AddCommandOperations
from apeiron.commons.help_messages import HelpMessages

from pathlib import Path
import os
import click
from pathlib import Path
import glob


@click.group(help='Command to  add <components>')
def init():
    pass

@init.command()
def project():
    if Apeiron.isapeiron():
        Message.warning('It is already an apeiron project!', label='')
    else:
        Apeiron.init()
        Message.report('Initialized empty Apeiron project in', Path(os.getcwd()).joinpath(Apeiron.apeirondir()).as_posix())
