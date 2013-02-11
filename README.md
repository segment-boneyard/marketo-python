marketo-python
==============

marketo-python is a python query client that wraps the Marketo SOAP API. For sending data to Marketo, check out [Segment.io](https://segment.io).

## Get Started

```
pip install marketo
```

```python
import marketo
client = marketo.Client(soap_endpoint='https://na-q.marketo.com/soap/mktows/2_0',
                        user_id='bigcorp1_461839624B16E06BA2D663',
                        encryption_key='899756834129871744AAEE88DDCC77CDEEDEC1AAAD66')
```

## Get Lead

This function retrieves a single lead record from Marketo.

```python
> lead = client.get_lead(email='ilya@segment.io')
<marketo.wrapper.lead_record.LeadRecord instance at 0x10855ec68>
> lead.id
'384563'
> lead.email
'ilya@segment.io'
> lead.attributes
{'Website': 'segment.io', 'Lead_Round_Robin_ID__c': 1, 'LeadStatus': 'Open', 'InferredCountry': 'United States', 'LeadScore': 20, 'FirstName': 'Ilya', 'AnonymousIP': '64.181.3.19', 'LastName': 'Volodarsky', 'Company': 'mkto', 'Created_Time__c': '2012-10-15 19:01:26Z', 'InferredCompany': 'Comcast Cable', 'Phone': '222-222-2222', 'Created_Timestamp__c': '2012-10-15T14:01:26-05:00', 'Lead_Assignment_Number__c': '3114', 'Referrer__c': 'drc'}
```

XML unwrapped [here](https://github.com/segmentio/marketo-python/blob/master/marketo/wrapper/lead_record.py).

## Get Lead Activity

```python
> activities = client.get_lead_activity(email='user@gmail.com')
[Activity (16095520 - Visit Webpage), Activity (16095507 - Click Link), Activity (16095506 - Click Link)]
> activity = activities[0]
> activity.id
'16095520'
> activity.type
'Visit Webpage'
> activity.attributes
{'Webpage ID': '20499', 'Message Id': '19122416', 'Webpage URL': '/pricing', 'Lead ID': '1474562', 'Query Parameters': None, 'Referrer URL': 'https://company.com/appointments/', 'Client IP Address': '61.183.85.141', 'User Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.57 Safari/537.17', 'Created At': '2013-02-11 16:19:48'}
```

XML unwrapped [here](https://github.com/segmentio/marketo-python/blob/master/marketo/wrapper/get_lead_activity.py).

### Error

An Exception is raised if the lead is not found, or if a Marketo error occurs.

```python
try:
    lead = client.get_lead(email='ilyaaaaaaa@segment.io')
except Exception as error:
    print error

'''
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"><SOAP-ENV:Body><SOAP-ENV:Fault><faultcode>SOAP-ENV:Client</faultcode><faultstring>20103 - Lead not found</faultstring><detail><ns1:serviceException xmlns:ns1="http://www.marketo.com/mktows/"><name>mktServiceException</name><message>No lead found with EMAIL = ilyaaaaaaa@segment.io (20103)</message><code>20103</code></ns1:serviceException></detail></SOAP-ENV:Fault></SOAP-ENV:Body></SOAP-ENV:Envelope>
'''
```



## License

```
WWWWWW||WWWWWW
 W W W||W W W
      ||
    ( OO )__________
     /  |           \
    /o o|    MIT     \
    \___/||_||__||_|| *
         || ||  || ||
        _||_|| _||_||
       (__|__|(__|__|
```

(The MIT License)

Copyright (c) 2012 Segment.io Inc. <friends@segment.io>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.