import requests
import json
from bs4 import BeautifulSoup
from xml.etree import ElementTree

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

def login_request(username, password):
    return {
            'grecaptcharesponse': 'Tk9UQVZBTElEQ0FQVENIQUZPUlRISVNSRVFVRVNU',
            'username': username,
            'password': password
        }

def login(username, password):
    url = 'http://VSMIIC230/generador-api/auth/login'
    headers = {'content-type': 'application/json'}
    raw_response = requests.post(url, json=login_request(username, password), headers=headers)
    json_response = json.loads(raw_response.content)
    return json_response['token']

def consultar_cvu(context):
    request = request_factory(context['cvu'])
    url = 'http://vsmiic230:80/cvu/ws/reporteExternoCvu'
    atemps = 5;
    while (atemps >0):
        headers = {'x-auth-token': context['token'], 'content-type': 'text/xml'}
        response = requests.post(url, data=request, headers=headers)
        errors = True
        soup = BeautifulSoup(response.content, features="lxml")
        root = ElementTree.fromstring(soup.prettify())
        for code in root.iter('archivo'):
                errors = False
        if(errors):
            context['token'] = login('gochihh@gmail.com','Rkk3NzMydW5AbQ==')
            atemps = atemps -1
        else:
            return root
