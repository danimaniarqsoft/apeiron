#! /usr/bin/env python
# -*- coding: utf-8 -*-
import click
from .message_type import MessageType

class Message:

    @staticmethod
    def content_added(*text):
        Message.simple_message('green', *text)
    
    @staticmethod
    def content_deleted(*text):
        Message.simple_message('bright_red', *text)

    @staticmethod
    def content_metadata(*text):
        Message.simple_message('blue', *text)
    
    @staticmethod
    def sucess(*text, sep=' ', label='\n'):
        Message.message('green', sep, label, *text)

    @staticmethod
    def console(*text, sep=' ', label='\n'):
        Message.message('green', sep, label, *text)

    @staticmethod
    def report(*text, sep=' ', label='\n'):
        Message.message('blue', sep, label, *text)

    @staticmethod
    def failure(*text, sep=' ', label='\n'):
        Message.message('bright_red', sep, label, *text)

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
    def simple_message(color, *text):
        Message.message(color, ' ', '', *text)

    @staticmethod
    def message(text_color, sep, label, *text):
        label_text = click.style(label, fg=text_color, bold=True)
        click.echo(label_text + click.style(sep.join(text), fg=text_color))
