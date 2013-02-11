import iso8601


class LeadActivity:

    def __init__(self):
        self.id = 'unknown'
        self.type = 'unknown'
        self.attributes = {}

    def __str__(self):
        return "Activity (%s - %s)" % (self.id, self.type)

    def __repr__(self):
        return self.__str__()


def unwrap(xml):
    activity = LeadActivity()
    activity.id = xml.find('id').text
    activity.timestamp = iso8601.parse_date(xml.find('activityDateTime').text)
    activity.type = xml.find('activityType').text

    for attribute in xml.findall('.//attribute'):
        name = attribute.find('attrName').text
        attr_type = attribute.find('attrType').text
        val = attribute.find('attrValue').text

        if attr_type == 'integer':
            val = int(val)

        activity.attributes[name] = val

    return activity
