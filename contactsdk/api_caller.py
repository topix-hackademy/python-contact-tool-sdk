import requests


class ContactSDKException(Exception):

    def __init__(self, resp):
        self.message = "Exception due to status code: %s" % resp.status_code


class ApiCaller(object):

    access_token = None
    base_url = None
    endpoint = None
    api_url = None

    def __init__(self, *args):
        self.access_token = args[0]
        self.base_url = args[1]
        self.endpoint = args[2]
        self.api_url = self.base_url + self.endpoint
        self._headers = {
            'content-type': 'application/json',
            'AUTH-TOKEN': self.access_token
        }

    def _wrapper_status_code(self, response):
        if response.status_code < 205:
            return response.json()
        raise ContactSDKException(response)

    def _get(self, resource):
        resp = requests.get(url="%s%s" % (self.api_url, resource),
                            data={},
                            headers=self._headers)
        return self._wrapper_status_code(resp)

    def _post(self, resource, _id, data):
        resp = requests.post(url="%s%s%s" % (self.api_url, resource, str(_id)),
                             data=data,
                             headers=self._headers)
        return self._wrapper_status_code(resp)

    def _update(self, resource, _id, data):
        resp = requests.put(url="%s%s%s" % (self.api_url, resource, str(_id)),
                            data=data,
                            headers=self._headers)
        return self._wrapper_status_code(resp)
