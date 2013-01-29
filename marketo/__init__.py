
import requests
import auth

from marketo.wrapper import get_lead


class Client:

    def __init__(self, soap_endpoint=None, user_id=None, encryption_key=None):

        if not soap_endpoint or not isinstance(soap_endpoint, str):
            raise ValueError('Must supply a soap_endpoint as a non empty string.')

        if not user_id or not isinstance(user_id, str):
            raise ValueError('Must supply a user_id as a non empty string.')

        if not encryption_key or not isinstance(encryption_key, str):
            raise ValueError('Must supply a encryption_key as a non empty string.')

        self.soap_endpoint = soap_endpoint
        self.user_id = user_id
        self.encryption_key = encryption_key

    def wrap(self, body):
        return (
            '<?xml version="1.0" encoding="UTF-8"?>' +
            '<env:Envelope xmlns:xsd="http://www.w3.org/2001/XMLSchema" ' +
                          'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" ' +
                          'xmlns:wsdl="http://www.marketo.com/mktows/" ' +
                          'xmlns:env="http://schemas.xmlsoap.org/soap/envelope/" ' +
                          'xmlns:ins0="http://www.marketo.com/mktows/" ' +
                          'xmlns:ns1="http://www.marketo.com/mktows/">' +
                auth.header(self.user_id, self.encryption_key) +
                '<env:Body>' +
                    body +
                '</env:Body>' +
            '</env:Envelope>')

    def request(self, body):
        envelope = self.wrap(body)
        response = requests.post(self.soap_endpoint, data=envelope,
            headers={
                'Connection': 'Keep-Alive',
                'Soapaction': '',
                'Content-Type': 'text/xml;charset=UTF-8',
                'Accept': '*/*'})
        return response

    def get_lead(self, email=None):

        if not email or not isinstance(email, str):
            raise ValueError('Must supply an email as a non empty string.')

        body = get_lead.wrap(email)
        response = self.request(body)
        if response.status_code == 200:
            return get_lead.unwrap(response)
        else:
            raise Exception(response.text)
