
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
