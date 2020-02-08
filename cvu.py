import click
from zeep import Client, Settings
from zeep.plugins import HistoryPlugin
import requests
from xml.etree import ElementTree
from bs4 import BeautifulSoup

def request_factory(cvu):
    return '''
        <soapenv:Envelope
            xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
            xmlns:rep="http://reporteexternocvu.conacyt.gob.mx">
            <soapenv:Header/>
            <soapenv:Body>
                <rep:reporteBytesEjecutivo>
                    <arg0>
                        <usuarioAplicativoCvuVO>
                            <numeroCvu>#{cvu}</numeroCvu>
                        </usuarioAplicativoCvuVO>
                    </arg0>
                </rep:reporteBytesEjecutivo>
            </soapenv:Body>
        </soapenv:Envelope>
        '''.replace("#{cvu}", str(cvu))

@click.command()
def cvu():
    namespaces = {
    'soap': 'http://schemas.xmlsoap.org/soap/envelope/',
    'a': 'http://www.etis.fskab.se/v1.0/ETISws',
    }
    request = request_factory(2)
    url = 'http://vsmiic230:80/cvu/ws/reporteExternoCvu'
    headers = {'x-auth-token': '34dd3ff2-02ea-4aca-a68c-9c217e8c607b', 'content-type': 'text/xml'}
    resp = requests.post(url, data=request, headers=headers)
    if resp.status_code != 200:
         print(resp.status_code)
    soup = BeautifulSoup(resp.content, features="lxml")
    print(soup.prettify())
    
if __name__ == '__main__':
    cvu()