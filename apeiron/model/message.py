import click
from .message_type import MessageType


class Message:

    @staticmethod
    def sucess(text):
        click.echo(click.style(text, fg='green'))

    @staticmethod
    def info(text):
        click.echo(click.style(text, fg='blue'))

    @staticmethod
    def warning(text):
        click.echo(click.style(text, fg='yellow'))

    @staticmethod
    def error(text):
        click.echo(click.style(text, fg='bright_red'))

    @staticmethod
    def message(type, text):
        if(type == MessageType.SUCCESS):
            Message.sucess(text)
        elif(type == MessageType.INFO):
            Message.info(text)
        elif(type == MessageType.WARNING):
            Message.warning(text)
        elif(type == MessageType.ERROR):
            Message.error(text)
        else:
            Message.info(text)
