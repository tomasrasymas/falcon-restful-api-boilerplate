import falcon
from utils.request_parser import parse
from schemas.group import GroupSchema
from models.group import Group
import marshmallow


class GroupsResource:
    def on_get(self, req, resp):
        all_groups = req.context.db_session.query(Group).all()

        resp.media = GroupSchema(many=True).dump(all_groups)
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        args = parse(schema=GroupSchema(partial=False,
                                        exclude=['id'],
                                        unknown=marshmallow.RAISE),
                     request=req)

        group = Group(**args)
        req.context.db_session.add(group)
        req.context.db_session.commit()

        resp.media = GroupSchema().dump(group)
        resp.status = falcon.HTTP_200
