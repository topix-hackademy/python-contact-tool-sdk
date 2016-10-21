import requests
import json


class ContactSDKException(Exception):

    response = None

    def __init__(self, resp):
        self.message = "Exception due to status code: %s" % resp.status_code
        self.response = resp


class ApiCaller(object):

    access_token = None
    base_url = None
    endpoint = None
    api_url = None
    _res = None

    def __init__(self, *args):
        self._res = args[0]
        self.access_token = args[1]
        self.base_url = args[2]
        self.endpoint = args[3]
        self.api_url = self.base_url + self.endpoint
        self._headers = {
            'content-type': 'application/json',
            'AUTH-TOKEN': self.access_token
        }

    def get_all(self):
        return self._get(self._res)

    def get_one(self, _id):
        return self._get("%s%s" % (self._res, str(_id)))

    def create(self, data):
        return self._post(self._res, data)

    def update(self, _id, data):
        return self._update(self._res, _id, data)

    def _get(self, resource):
        try:
            resp = requests.get(url="%s%s" % (self.api_url, resource),
                                data={},
                                headers=self._headers)
        except Exception as e:
            resp=None
        return ApiCaller._wrapper_status_code(resp)

    def _post(self, resource, data):
        resp = requests.post(url="%s%s" % (self.api_url, resource),
                             data=json.dumps(data),
                             headers=self._headers)
        return ApiCaller._wrapper_status_code(resp)

    def _update(self, resource, _id, data):
        resp = requests.put(url="%s%s%s/" % (self.api_url, resource, str(_id)),
                            data=json.dumps(data),
                            headers=self._headers)
        return ApiCaller._wrapper_status_code(resp)

    @staticmethod
    def _wrapper_status_code(response):
        if response:
            if response.status_code < 205:
                return response.json()
        else:
            response.status_code="connection error"
        raise ContactSDKException(response)


class ContactApiCaller(ApiCaller):

    def get_by_email(self, email):
        return self._get("contact-by-email/%s/" % email)
        
    def get_by_csid(self, csid):
        return self._get("contact-by-csid/%s/" % csid)
    

class CompanyApiCaller(ApiCaller):

    def get_by_code(self, code):
        return self._get("company-by-code/%s/" % code)

    def get_by_csid(self, csid):
        return self._get("company-by-csid/%s/" % csid)

    def get_freesearch(self, searchstring):
        return self._get("company-freesearch/%s/" % searchstring)
