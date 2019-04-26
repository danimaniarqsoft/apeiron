#! /usr/bin/env python
# -*- coding: utf-8 -*-
import click
from .message_type import MessageType


class Message:

    @staticmethod
    def sucess(*text, sep=' ', label=''):
        Message.message('green', sep, label, *text)
        
    @staticmethod
    def info(*text, sep=' ', label='[ INFO  ] '):
        Message.message('blue', sep, label, *text)

    @staticmethod
    def warning(*text, sep=' ', label="[WARNING] "):
        Message.message('bright_yellow', sep, label, *text)

    @staticmethod
    def error(*text, sep=' ', label='[ ERROR ] '):
        Message.message('bright_red', sep, label, *text)

    @staticmethod
    def message(text_color, sep, label, *text):
        label_text = click.style(label, fg=text_color, bold=True)
        click.echo(label_text + click.style(sep.join(text), fg=text_color))
