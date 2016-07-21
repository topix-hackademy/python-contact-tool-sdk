from contactsdk.api_caller import ApiCaller

class CompanyType(ApiCaller):
    _res = 'company-type/'

    def __init__(self, *args, **kw):
        super(CompanyType, self).__init__(*args, **kw)

    def get_all(self):
        return self._get(self._res)

    def get_one(self, _id):
        return self._get("%s%s" % (self._res, str(_id)))

    def create(self, data):
        return self._post(self._res, data)

    def update(self, _id, data):
        return self._update(self._res, _id, data)


class Company(ApiCaller):

    _res = 'company/'

    def __init__(self, *args, **kw):
        super(Company, self).__init__(*args, **kw)

    def get_all(self):
        return self._get(self._res)

    def get_one(self, _id):
        return self._get("%s%s" % (self._res, str(_id)))

    def create(self, data):
        return self._post(self._res, data)

    def update(self, _id, data):
        return self._update(self._res, _id, data)
