from sqlalchemy.orm.query import Query


class BaseQueryBuilder:
    def __init__(self, entities):
        self.query = Query(entities)

    def build(self):
        return self.query
