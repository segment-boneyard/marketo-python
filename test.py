
import unittest

import marketo
import marketo.auth


class MarketoBasicTests(unittest.TestCase):

    def test_auth(self):
        # From Marketo example"
        user_id = "bigcorp1_461839624B16E06BA2D663"
        encryption_key = "899756834129871744AAEE88DDCC77CDEEDEC1AAAD66"
        timestamp = "2010-04-09T14:04:54-07:00"
        signature = "ffbff4d4bef354807481e66dc7540f7890523a87"
        self.assertTrue(marketo.auth.sign(timestamp + user_id, encryption_key) == signature)

    def test_lead_activity(self):
        client = marketo.Client(soap_endpoint='https://na-q.marketo.com/soap/mktows/2_0',
                                user_id='drchrono1_07236202501971D13A8732',
                                encryption_key='6859529233869019550011997711DD2333ABE6B62621')

        activities = client.get_lead_activity(email='che@drchrono.com')
        import pdb; pdb.set_trace()

if __name__ == '__main__':
    unittest.main()
