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
from fpdf import FPDF

from pathlib import Path


@click.group(help='Command to  add <components>')
def add():
    pass


@add.command()
@click.option('--email', default="none@noe.com", prompt='Email',
              help="Add a Contributing File")
@click.option('--force', '-f', is_flag=True)
@click.pass_context
def contributing_file(ctx, email, force):
    ctx.obj['email']= email
    if AddCommandOperations.add(email, force):
        Message.sucess("Contributing file was added!")
    else:
        Message.failure("Conflict must be resolved")

@add.command()
@click.option('--email', default="none@noe.com", prompt='Email',
              help="Add a Contributing File")
def pdf(email):
    model = {"email": email}
    text = TemplateManager.fill('CONTRIBUTING.md', model)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.text(200, 10, txt=text)
    #pdf.cell(200, 10, txt=text, ln=1, align="C")
    pdf.output("simple_demo.pdf")
