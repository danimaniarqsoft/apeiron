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
import matplotlib.pyplot as plt

choices = ['scatter', 'line', 'bar']

@click.group(help='Command to  add <components>')
def plot():
    pass

@plot.command()
@click.option('--type', default='line', type=click.Choice(choices),
              help="Add a Contributing File")
def pdf(type):
    print("selected: " + type)
