import falcon


def handler(ex, req, resp, params):
    if not isinstance(ex, ErrorBase):
        if isinstance(ex, falcon.HTTPError):
            raise ErrorBase(title=ex.title or 'HTTP exception',
                            description=ex.description or 'No more details',
                            status=falcon.HTTP_404,
                            errors={},
                            code=-1)
        else:
            raise ErrorBase(title='Unhandled exception',
                            description=str(ex),
                            status=falcon.HTTP_404,
                            errors={},
                            code=-1)

    raise ex


class ErrorBase(falcon.HTTPError):
    def __init__(self, title, description, status, errors, code):
        super().__init__(status=status,
                         title=title,
                         description=description,
                         code=code)

        self._errors = errors

    def to_dict(self, obj_type=dict):
        result = {'title': (self.title or 'HTTP exception'),
                  'description': (self.description or 'No more details'),
                  'errors': (self._errors or {}),
                  'code': (self.code or -1)}
        return result


class RequestParsingError(ErrorBase):
    def __init__(self, description, errors=None):
        super().__init__(status=falcon.HTTP_404,
                         title='Request parsing error',
                         description=description,
                         code=1,
                         errors=errors or {})


class ModelAttrError(ErrorBase):
    def __init__(self, description, errors=None):
        super().__init__(status=falcon.HTTP_404,
                         title='Model attribute error',
                         description=description,
                         code=1,
                         errors=errors or {})


class EntityNotExists(ErrorBase):
    def __init__(self, description, errors=None):
        super().__init__(status=falcon.HTTP_404,
                         title='Entity not exists',
                         description=description,
                         code=1,
                         errors=errors or {})


class EntityExists(ErrorBase):
    def __init__(self, description, errors=None):
        super().__init__(status=falcon.HTTP_404,
                         title='Entity exists',
                         description=description,
                         code=1,
                         errors=errors or {})