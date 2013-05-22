
def wrap(campaign=None, lead=None):
    return (
        '<mkt:paramsRequestCampaign>' +
            '<source>MKTOWS</source>' +
            '<campaignId>' + campaign + '</campaignId>' +
            '<leadList>' +
                '<leadKey>' +
                    '<keyType>IDNUM</keyType>' +
                    '<keyValue>' + lead + '</keyValue>' +
                '</leadKey>' +
            '</leadList>' +
        '</mkt:paramsRequestCampaign>')
