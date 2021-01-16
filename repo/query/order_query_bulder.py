from entity.customer import Customer
from entity.order import Order
from repo.query.base_query_bulder import BaseQueryBuilder


class OrderQueryBuilder(BaseQueryBuilder):
    def __init__(self):
        super().__init__([Order])
        self.query = self.query.join(Customer)

    def cust_first_name(self, first_name):
        if first_name:
            self.query = self.query.filter(
                Customer.contactFirstName == first_name
            )
        return self

    def cust_last_name(self, last_name):
        if last_name:
            self.query = self.query.filter(
                Customer.contactLastName == last_name
            )
        return self

    def order_by_date(self, enabled):
        if enabled:
            self.query = self.query.order_by(Order.orderDate)
        return self

    def order_by_cust_last_name(self, enabled):
        if enabled:
            self.query = self.query.order_by(Customer.contactLastName)
        return self
