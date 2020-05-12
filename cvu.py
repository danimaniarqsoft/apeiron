import click
import requests
from xml.etree import ElementTree
from base64 import b64decode
from util import consultar_cvu, login
import csv

@click.command()
def cvu():
    context = {'token': login('gochihh@gmail.com','Rkk3NzMydW5AbQ=='), 'cvu': 0}
    destination_path = '/home/daniel/Desktop/cvu/'
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
                    bytes = b64decode(repo.text, validate=False)
                    file_name = destination_path + str(context['cvu']) + '.pdf' 
                    f = open(file_name, 'wb')
                    f.write(bytes)
                    f.close()
                if(file_exist):
                    writer.writerow([context['cvu'], 'success'])
                    print(context['cvu'] + ', success')
                else:
                    writer.writerow([context['cvu'], ', fail'])
                    print(context['cvu'] + ', fail')

if __name__ == '__main__':
    cvu()