import falcon


class RequireJson:
    def process_request(self, req, resp):
        if not req.client_accepts_json:
            raise falcon.HTTPNotAcceptable(description='This API only supports responses encoded as JSON.')

        if req.method in ('POST', 'PUT'):
            if 'application/json' not in req.content_type:
                raise falcon.HTTPUnsupportedMediaType(description='This API only supports requests encoded as JSON.')