"""
Generate PDF reports from trello json
""" 
import json
from collections import namedtuple
from jinja2 import Template, Environment, FileSystemLoader
import apeiron.reader as r
import click
#from apeiron.reader import add

from fpdf import FPDF

def createPdf():
    pdf = FPDF(orientation='P', unit='mm', format='letter')
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Reporte informativo", ln=1, align="C")
    pdf.output("demo_pdf.pdf")

def run():
    with open('apeiron/resources/data.json', 'r', encoding='utf8') as json_file:
        data = json.load(json_file)
    print(data['name'])
    for card in data['cards']:
        print(card['name'])
    #createPdf()
    template = Template('Hello {{ name }}!')
    template.render(name='John Doe')
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template("apeiron/resources/templates/report.html")
    print(template.render(title='REPORTE SEMANAL'))

def forTest():
    return None

@click.command()
@click.option("--number", prompt="factorial number",
              help="The index of the factorial number")
def calculate(data):
    for item in data:
        print(item)

def sort(numbers):
    for item in numbers:
        print(item)

if __name__ == "__main__":
    numbers = [2,3,9,3,7,6]
    # execute only if run as a script
    sort(numbers)


