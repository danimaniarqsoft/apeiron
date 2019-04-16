"""
Generate PDF reports from trello json
""" 
import json
from collections import namedtuple
from jinja2 import Template, Environment, FileSystemLoader
import apeiron.reader as r
import click

@click.group()
def cli():
    pass

@click.command()
@click.option("--n", default=1, prompt="factorial number", help="The number of the factorial")
def factorial(n):
    print(fact(int(n)))

@click.command()
@click.option("--m", default="[no message]", prompt="common message", help="print a common messsage")
def message(m):
    print(m)

@click.command()
@click.option('--password', prompt=True, confirmation_prompt=True,
              hide_input=True)
def changeadmin(password):
    pass

def fact(n):
    if(n<2):
        return 1
    else:
        return n*fact(n-1)

cli.add_command(factorial)
cli.add_command(message)
cli.add_command(changeadmin)
