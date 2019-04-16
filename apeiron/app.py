"""
Generate PDF reports from trello json
""" 
import json
from collections import namedtuple
from jinja2 import Template, Environment, FileSystemLoader
import apeiron.reader as r
import click
#from apeiron.reader import add

@click.command()
@click.option("--n", default=1, prompt="factorial number", help="The number of the factorial")
def cli(n):
    print(factorial(n))

def factorial(n):
    if(n<2):
        return 1
    else:
        return n*factorial(n-1)
