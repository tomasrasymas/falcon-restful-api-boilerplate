import falcon


class ApiIndexResource:
    def on_get(self, req, resp):
        resp.media = {'api': 'ok'}
        resp.status = falcon.HTTP_200
