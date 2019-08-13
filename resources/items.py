import falcon
from utils.request_parser import parse
from schemas.item import ItemSchema
from models.item import Item
import marshmallow


class ItemsResource:
    def on_get(self, req, resp):
        all_items = req.context.db_session.query(Item).all()

        resp.media = ItemSchema(many=True).dump(all_items)
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        args = parse(schema=ItemSchema(partial=False,
                                       exclude=['id'],
                                       unknown=marshmallow.RAISE),
                     request=req)

        item = Item(**args)
        req.context.db_session.add(item)
        req.context.db_session.commit()

        resp.media = ItemSchema().dump(item)
        resp.status = falcon.HTTP_200
