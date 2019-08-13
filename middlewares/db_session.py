class DbSessionManager:
    def __init__(self, Session):
        self.db_session = Session

    def process_resource(self, req, resp, resource, params):
        if req.method == 'OPTIONS':
            return

        req.context.db_session = self.db_session()

    def process_response(self, req, resp, resource, req_succeeded):
        if req.method == 'OPTIONS':
            return

        if hasattr(req.context, 'db_session'):
            if not req_succeeded:
                req.context.db_session.rollback()
            req.context.db_session.close()
