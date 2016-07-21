from contactsdk.api_caller import ApiCaller

class Contact(ApiCaller):
    _res = 'contact/'

    def __init__(self, *args, **kw):
        super(Contact, self).__init__(*args, **kw)

    def get_all(self):
        return self._get(self._res)

    def get_one(self, _id):
        return self._get("%s%s" % (self._res, str(_id)))

    def create(self, data):
        pass

    def update(self, data):
        pass

class ContactType(ApiCaller):
    _res = 'role/'

    def __init__(self, *args, **kw):
        super(ContactType, self).__init__(*args, **kw)

    def get_all(self):
        return self._get(self._res)

    def get_one(self, _id):
        return self._get("%s%s" % (self._res, str(_id)))

    def create(self, data):
        pass

    def update(self, data):
        pass
