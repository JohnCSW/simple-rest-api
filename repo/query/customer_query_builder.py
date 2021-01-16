from .base_query_bulder import BaseQueryBuilder
from entity.customer import Customer


class CustomerQueryBuilder(BaseQueryBuilder):
    def __init__(self):
        super().__init__([Customer])

    def first_name(self, first_name):
        if first_name:
            self.query = self.query.filter(
                Customer.contactFirstName == first_name
            )
        return self

    def last_name(self, last_name):
        if last_name:
            self.query = self.query.filter(
                Customer.contactLastName == last_name
            )
        return self

    def order_by_credit_limit(self, enabled):
        if enabled:
            self.query = self.query.order_by(Customer.creditLimit)
        return self
