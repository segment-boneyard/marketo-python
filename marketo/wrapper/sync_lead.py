
import xml.etree.ElementTree as ET
import lead_record


def wrap(email=None, attributes=None):
    attr = ''
    for i in attributes:
        attr += '<attribute>' \
            '<attrName>' + i[0] + '</attrName>' \
            '<attrType>' + i[1] + '</attrType>' \
            '<attrValue>' + i[2] + '</attrValue>' \
            '</attribute>'

    return(
        '<mkt:paramsSyncLead>' +
        '<leadRecord>' +
        '<Email>' + email + '</Email>' +
        '<leadAttributeList>' + attr + '</leadAttributeList>' +
        '</leadRecord>' +
        '<returnLead>true</returnLead>' +
        '<marketoCookie></marketoCookie>' +
        '</mkt:paramsSyncLead>'
    )


def unwrap(response):
    root = ET.fromstring(response.text)
    lead_record_xml = root.find('.//leadRecord')
    return lead_record.unwrap(lead_record_xml)
