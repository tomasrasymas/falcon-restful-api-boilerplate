import falcon
from utils.request_parser import parse
from schemas.group import GroupSchema
from models.group import Group
import marshmallow
from utils.exceptions import EntityNotExists


class GroupResource:
    def on_get(self, req, resp, id):
        group = req.context.db_session.query(Group).get(id)

        if not group:
            raise EntityNotExists(description='Group with id=%s not exists' % id)

        resp.media = GroupSchema().dump(group)
        resp.status = falcon.HTTP_200

    def on_patch(self, req, resp, id):
        args = parse(schema=GroupSchema(partial=True,
                                        exclude=['id'],
                                        unknown=marshmallow.RAISE),
                     request=req)

        group = req.context.db_session.query(Group).get(id)

        if not group:
            raise EntityNotExists(description='Group with id=%s not exists' % id)

        group.update(**args)

        req.context.db_session.add(group)
        req.context.db_session.commit()

        resp.media = GroupSchema().dump(group)
        resp.status = falcon.HTTP_200

    def on_delete(self, req, resp, id):
        group = req.context.db_session.query(Group).get(id)
        req.context.db_session.delete(group)
        req.context.db_session.commit()

        resp.media = GroupSchema().dump(group)
        resp.status = falcon.HTTP_200
