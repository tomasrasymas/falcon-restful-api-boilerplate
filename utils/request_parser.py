from falcon import request
from marshmallow import schema
from utils.exceptions import RequestParsingError


def parse(schema: schema, request: request) -> (dict, dict):
    result = {}
    try:
        result = schema.load(data=request.media)
    except Exception as e:
        if not result:
            if hasattr(e, 'messages'):
                result = e.messages

        raise RequestParsingError(description='Unable to parse request body into schema object. %s' % str(e),
                                  errors=result)

    return result
