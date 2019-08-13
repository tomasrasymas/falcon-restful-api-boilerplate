import falcon
from schemas.item import ItemSchema
from models.group import Group
from utils.exceptions import EntityNotExists


class GroupItemsResource:
    def on_get(self, req, resp, group_id):
        group = req.context.db_session.query(Group).get(group_id)

        if not group:
            raise EntityNotExists(description='Group with id=%s not exists' % group_id)

        resp.media = ItemSchema(many=True, exclude=['groups']).dump(group.items)
        resp.status = falcon.HTTP_200
