import falcon
from schemas.group import GroupSchema
from models.group import Group
from models.item import Item
from utils.exceptions import EntityNotExists, EntityExists


class GroupItemResource:
    def on_post(self, req, resp, group_id, item_id):
        group = req.context.db_session.query(Group).get(group_id)
        item = req.context.db_session.query(Item).get(item_id)

        if not group:
            raise EntityNotExists(description='Group with id=%s not exists' % group_id)

        if not item:
            raise EntityNotExists(description='Item with id=%s not exists' % item_id)

        if item in group.items:
            raise EntityExists(description='Group %s already has item id=%s assigned' % (group_id, item_id))

        group.items.append(item)
        req.context.db_session.commit()

        resp.media = GroupSchema().dump(group)
        resp.status = falcon.HTTP_200

    def on_delete(self, req, resp, group_id, item_id):
        group = req.context.db_session.query(Group).get(group_id)
        item = req.context.db_session.query(Item).get(item_id)

        if not group:
            raise EntityNotExists(description='Group with id=%s not exists' % group_id)

        if not item:
            raise EntityNotExists(description='Item with id=%s not exists' % item_id)

        if item not in group.items:
            raise EntityNotExists(description='Group %s has no item with id=%s assigned' % (group_id, item_id))

        group.items.remove(item)
        req.context.db_session.commit()

        resp.media = GroupSchema().dump(group)
        resp.status = falcon.HTTP_200
