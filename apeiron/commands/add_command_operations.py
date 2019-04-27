#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Main Command Line Interface for Plugin Management
"""
import os
import click
from pathlib import Path
from pkg_resources import iter_entry_points
from click_plugins import with_plugins
from apeiron.commons import Message, Files, FileVersionManager
from apeiron.core import TemplateManager
from pathlib import Path


class AddCommandOperations:
    @staticmethod
    def add(email, force_override=False):
        model = {"email": email}
        text = TemplateManager.fill('CONTRIBUTING.md', model)
        return Files.save(text, Path(os.getcwd()),
                          'CONTRIBUTING_borrar.md', force_override)
