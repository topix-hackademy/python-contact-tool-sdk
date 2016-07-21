from contactsdk.api_caller import ApiCaller


class Connector(object):

    _instance = None

    def __init__(self, access_token=None, base_url=None, endpoint=None):
        if not access_token or not base_url or not endpoint:
            raise Exception("All Arguments are required in format: %s" % Connector._print_how_to())

        if not self._instance:
            self._instance = super(Connector, self).__init__()

        self.access_token = access_token
        self.base_url = Connector.__add_ending_slash(base_url)
        self.endpoint = Connector.__add_ending_slash(endpoint)

        self.company = ApiCaller('company/', access_token, base_url, endpoint)
        self.company_type = ApiCaller('company-type/', access_token, base_url, endpoint)
        self.contact = ApiCaller('contact/', access_token, base_url, endpoint)
        self.contact_type = ApiCaller('role/', access_token, base_url, endpoint)

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
'''.format(access_token=self.access_token, base_url=self.base_url, endpoint=self.endpoint)

    @staticmethod
    def _print_how_to():
        return "c = Connector(ACCESS-TOKEN, ENDPOINT, URL)"

    @staticmethod
    def __add_ending_slash(path):
        if not path.endswith('/'):
            path += '/'
        return path
