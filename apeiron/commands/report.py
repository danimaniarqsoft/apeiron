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
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle



choices = ['scatter', 'line', 'bar']

@click.group(help='Command to  report <type of report>')
def report():
    pass

@report.command()
def pdf():
    w, h = letter
    c = canvas.Canvas("hola-mundo.pdf", pagesize=letter)

    text = c.beginText(50, h - 50)
    text.setFont("Times-Roman", 12)
    text.textLine("¡Hola, mundo!")
    text.textLine("¡Hola, mundo!")
    text.textLine("¡Hola, mundo!")
    c.drawText(text)
    c.showPage()
    c.save()