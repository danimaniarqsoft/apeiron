import click
from zeep import Client, Settings
from zeep.plugins import HistoryPlugin
import requests
from xml.etree import ElementTree
from bs4 import BeautifulSoup
from base64 import b64decode
from util import request_factory
import csv


@click.command()
def cvu():
    url = 'http://vsmiic230:80/cvu/ws/reporteExternoCvu'
    headers = {'x-auth-token': '40356181-a406-4df0-9629-6d18606b17da', 'content-type': 'text/xml'}
    destination_path = '/home/daniel/Desktop/'
    
    with open('data.csv', mode='r') as infile:
        reader = csv.reader(infile)
        next(reader, None)  # skip the headers
        with open('result.csv', mode='w') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(['cvu', 'status'])
            for rows in reader:
                cvu_number = rows[0]
                request = request_factory(cvu_number)
                resp = requests.post(url, data=request, headers=headers)
                if resp.status_code != 200:
                    print(resp.status_code)
                    writer.writerow([cvu_number, 'fail'])
                    print(cvu_number + ', fail')
                else:
                    soup = BeautifulSoup(resp.content, features="lxml")
                    root = ElementTree.fromstring(soup.prettify())
                    file_exist = False
                    for repo in root.iter('archivo'):
                        file_exist = True
                        bytes = b64decode(repo.text, validate=False)
                        file_name = destination_path + str(cvu_number) + '.pdf' 
                        f = open(file_name, 'wb')
                        f.write(bytes)
                        f.close()
                    if(file_exist):
                        writer.writerow([cvu_number, 'success'])
                        print(cvu_number + ', success')
                    else:
                        writer.writerow([cvu_number, ', fail'])
                        print(cvu_number + ', fail')

if __name__ == '__main__':
    cvu()