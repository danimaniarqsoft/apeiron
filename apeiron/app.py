"""
Main Command Line Interface for Plugin Management
""" 
from pkg_resources import iter_entry_points

import click
from click_plugins import with_plugins

@with_plugins(iter_entry_points('apeirion.plugins'))
@click.group()
def cli():
    """
    This is the default CLI command.
    \b
        For add new plugins, please read the documentation
    \b
    """

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
