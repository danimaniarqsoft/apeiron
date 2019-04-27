#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Main Command Line Interface for Plugin Management
"""
from jinja2 import Environment, PackageLoader, select_autoescape


class TemplateManager:

    _env = Environment(loader=PackageLoader('apeiron', 'resources/templates', encoding='utf-8'), autoescape=select_autoescape(['html', 'xml']))

    @classmethod
    def fill(self, template, model):
        template = self._env.get_template(template)
        return template.render(model)
