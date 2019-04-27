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
from apeiron.commands.add import add
from apeiron.commands.clean import clean
from apeiron.commands.show import show
from apeiron.commands.init import init
from pathlib import Path


@with_plugins(iter_entry_points('apeirion.plugins'))
@click.group()
def cli():
    pass


cli.add_command(add)
cli.add_command(clean)
cli.add_command(show)
cli.add_command(init)
