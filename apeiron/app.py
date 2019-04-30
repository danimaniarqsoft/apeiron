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
from apeiron.commands.plot import plot
from apeiron.commands.report import report

from pathlib import Path

commands = [add, clean, show, init, plot, report]

@with_plugins(iter_entry_points('apeirion.plugins'))
@click.group()
def cli():
    pass


for command in commands:
    cli.add_command(command)