import json
from collections import namedtuple
from jinja2 import Template, Environment, FileSystemLoader
from weasyprint import HTML

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

