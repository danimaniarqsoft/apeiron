import os
import click
import base64
import requests
from pathlib import Path
from xml.etree import ElementTree
from base64 import b64decode
from builtins import bytes
from util import consultar_cvu, login
import csv

@click.command()
@click.option('--path', default=os.environ['HOME'], help='ruta en la que se generarán los reportes de cvu')
@click.option('--user', help='usuario cvu con el que se iniciará sesión')
@click.password_option(help='contraseña con la que inicia sesión')
def cvu(path, user, password):
    password = str(base64.b64encode(password.encode('utf-8')), 'utf-8')
    print(password)
    context = {'token': login(user, password), 'cvu': 0}
    destination_path = path + '/cvu/'
    Path(destination_path).mkdir(parents=True, exist_ok=True)
    with open('data.csv', mode='r') as infile:
        reader = csv.reader(infile)
        next(reader, None)  # skip the headers
        with open('result.csv', mode='w') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(['cvu', 'status'])
            for row in reader:
                context['cvu']= row[0]
                root = consultar_cvu(context)
                file_exist = False
                for repo in root.iter('archivo'):
                    file_exist = True
                    bytes_decoded = b64decode(repo.text, validate=False)
                    file_name = destination_path + str(context['cvu']) + '.pdf' 
                    f = open(file_name, 'wb')
                    f.write(bytes_decoded)
                    f.close()
                if(file_exist):
                    writer.writerow([context['cvu'], 'success'])
                    print(context['cvu'] + ', success')
                else:
                    writer.writerow([context['cvu'], ', fail'])
                    print(context['cvu'] + ', fail')

if __name__ == '__main__':
    cvu()