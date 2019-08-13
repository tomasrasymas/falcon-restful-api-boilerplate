import falcon
from utils.request_parser import parse
from schemas.item import ItemSchema
from models.item import Item
import marshmallow
from utils.exceptions import EntityNotExists


class ItemResource:
    def on_get(self, req, resp, id):
        item = req.context.db_session.query(Item).get(id)

        if not item:
            raise EntityNotExists(description='Item with id=%s not exists' % id)

        resp.media = ItemSchema().dump(item)
        resp.status = falcon.HTTP_200

    def on_patch(self, req, resp, id):
        args = parse(schema=ItemSchema(partial=True,
                                       exclude=['id'],
                                       unknown=marshmallow.RAISE),
                     request=req)

        item = req.context.db_session.query(Item).get(id)

        if not item:
            raise EntityNotExists(description='Item with id=%s not exists' % id)

        item.update(**args)

        req.context.db_session.add(item)
        req.context.db_session.commit()

        resp.media = ItemSchema().dump(item)
        resp.status = falcon.HTTP_200

    def on_delete(self, req, resp, id):
        item = req.context.db_session.query(Item).get(id)
        req.context.db_session.delete(item)
        req.context.db_session.commit()

        resp.media = ItemSchema().dump(item)
        resp.status = falcon.HTTP_200
