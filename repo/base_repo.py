from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Query

from entity.customer import Customer

engine = create_engine(
    'mysql+pymysql://root:for-root-test-only@localhost:3306/classicmodels'
)
Session = sessionmaker(bind=engine)


class BaseRepo:
    def __init__(self):
        self.session = Session()

    def find_all(self, query):
        return query.with_session(self.session).all()
