from entity.employee import Employee
from repo.query.base_query_bulder import BaseQueryBuilder


class EmployeeQueryBuilder(BaseQueryBuilder):
    def __init__(self):
        super().__init__([Employee])

    def first_name(self, first_name):
        if first_name:
            self.query = self.query.filter(
                Employee.firstName == first_name
            )
        return self

    def last_name(self, last_name):
        if last_name:
            self.query = self.query.filter(
                Employee.lastName == last_name
            )
        return self

    def order_by_last_name(self, enabled):
        if enabled:
            self.query = self.query.order_by(Employee.lastName)
        return self
