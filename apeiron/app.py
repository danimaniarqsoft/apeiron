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

from pathlib import Path

@with_plugins(iter_entry_points('apeirion.plugins'))
@click.group()
def cli():
    pass

cli.add_command(add)
cli.add_command(clean)

if __name__ == "__main__":    
    text1 = open("CONTRIBUTING.md").readlines()
    text2 = open("CONSTRIBUTING_borrar.md").readlines()
    for line in difflib.unified_diff(text1, text2):
        print (line)