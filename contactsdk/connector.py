from contactsdk.company import Company, CompanyType
from contactsdk.contact import Contact, ContactType

class Connector(object):

    _instance = None

    access_token = None
    base_url = None
    endpoint = None
    company = Company()
    company_type = CompanyType()
    contact = Contact()
    contact_type = ContactType()

    def __init__(self, access_token=None, base_url=None, endpoint=None):
        if not access_token or not base_url or not endpoint:
            raise Exception("All Arguments are required in format: %s" % self.print_how_to())

        if not self._instance:
            self._instance = super(Connector, self).__init__()

        self.access_token = access_token
        self.base_url = base_url
        self.endpoint = endpoint

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return '''
ACCESS-TOKEN:
    {access_token}
BASE-URL:
    {base_url}
ENDPOINT:
    {endpoint}
'''.format(access_token=self.access_token,
                   base_url=self.base_url,
                   endpoint=self.endpoint)

    def print_how_to(self):
        return "c = Connector(ACCESS-TOKEN, ENDPOINT, URL)"
