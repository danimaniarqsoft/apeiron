import click
import zeep

@click.command()
def cvu():
    wsdl = 'http://www.soapclient.com/xml/soapresponder.wsdl'
    client = zeep.Client(wsdl=wsdl)
    print(client.service.Method1('consultar', 'cvu'))

if __name__ == '__main__':
    cvu()