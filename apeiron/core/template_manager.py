#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Main Command Line Interface for Plugin Management
"""
from jinja2 import Environment, PackageLoader, select_autoescape

class TemplateManager:

    def __init__(self):
        self.env = Environment(
        loader=PackageLoader('apeiron', 'resources/templates', encoding='utf-8'),
        autoescape=select_autoescape(['html', 'xml']))

    def fill(self, template):
        template = self.env.get_template(template)
        return template.render(title='work', body='well')
