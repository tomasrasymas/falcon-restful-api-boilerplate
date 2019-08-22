import falcon
from resources.api_index import ApiIndexResource
from resources.groups import GroupsResource
from resources.group import GroupResource
from resources.items import ItemsResource
from resources.item import ItemResource
from resources.group_items import GroupItemsResource
from resources.group_item import GroupItemResource
from utils.exceptions import handler
from middlewares.db_session import DbSessionManager
from db import Session


def get_app() -> falcon.API:
    app = falcon.API(middleware=[DbSessionManager(Session=Session)])

    app.add_route('/api', ApiIndexResource())
    app.add_route('/api/groups', GroupsResource())
    app.add_route('/api/groups/{id}', GroupResource())
    app.add_route('/api/items', ItemsResource())
    app.add_route('/api/items/{id}', ItemResource())
    app.add_route('/api/group/{group_id}/items', GroupItemsResource())
    app.add_route('/api/group/{group_id}/items/{item_id}', GroupItemResource())

    app.add_error_handler(exception=Exception, handler=handler)

    return app


if __name__ == '__main__':
    from wsgiref import simple_server
    with simple_server.make_server('', 8080, get_app()) as httpd:
        httpd.serve_forever()
