import sys
#sys.path.append('C:\\Users\\daniel.cortes\\development\\git\\apeiron-cli\\apeiron-cli\\reader')
import json
from collections import namedtuple

#from apeiron.reader import add

from fpdf import FPDF

def createPdf():
    pdf = FPDF(orientation='P', unit='mm', format='letter')
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Reporte informativo", ln=1, align="C")
    pdf.output("demo_pdf.pdf")

def run():
    with open('data.json') as json_file:
        data = json.load(json_file)
    print(data['id'])
    #createPdf()
