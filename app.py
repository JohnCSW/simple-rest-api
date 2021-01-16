from flask import Flask, request

from common.entity_serializer import serialize_entity
from repo.base_repo import BaseRepo
from repo.product_repo import ProductRepo
from repo.query.customer_query_builder import CustomerQueryBuilder
from repo.query.employee_query_builder import EmployeeQueryBuilder
from repo.query.order_query_bulder import OrderQueryBuilder

app = Flask(__name__)


@app.route('/api/customers', methods=['GET'], endpoint='find_customers')
@serialize_entity
def find_customers():
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    orderCriteria = request.args.get('order_by')
    queryBuilder = CustomerQueryBuilder()
    query = queryBuilder \
        .first_name(first_name) \
        .last_name(last_name) \
        .order_by_credit_limit(orderCriteria == 'credit_limit') \
        .build()
    customerRepo = BaseRepo()
    customers = customerRepo.find_all(query)
    return customers


@app.route('/api/employees', methods=['GET'], endpoint='find_employees')
@serialize_entity
def find_employees():
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    orderCriteria = request.args.get('order_by')
    queryBuilder = EmployeeQueryBuilder()
    query = queryBuilder \
        .first_name(first_name) \
        .last_name(last_name) \
        .order_by_last_name(orderCriteria == 'last_name') \
        .build()
    employeeRepo = BaseRepo()
    customers = employeeRepo.find_all(query)
    return customers


@app.route('/api/orders', methods=['GET'], endpoint='find_orders')
@serialize_entity
def find_orders():
    cust_first_name = request.args.get('first_name')
    cust_last_name = request.args.get('last_name')
    orderCriteria = request.args.get('order_by')
    queryBuilder = OrderQueryBuilder()
    query = queryBuilder \
        .cust_first_name(cust_first_name) \
        .cust_last_name(cust_last_name) \
        .order_by_date(orderCriteria == 'date') \
        .order_by_cust_last_name(orderCriteria == 'last_name') \
        .build()
    orderRepo = BaseRepo()
    customers = orderRepo.find_all(query)
    return customers

@app.route('/api/products', methods=['POST'], endpoint='create_product')
@serialize_entity
def create_proudct():
    """
    example input:
    {
        "MSRP": 95.7,
        "buyPrice": 48.81,
        "productCode": "S10_2022",
        "productDescription": "This replica features working kickstand, front suspension, gear-shift lever, footbrake lever, drive chain, wheels and steering. All parts are particularly delicate due to their precise scale and require special care and attention.",
        "productLine": "Motorcycles",
        "productName": "1969 Harley Davidson Ultimate Chopper",
        "productScale": "1:10",
        "productVendor": "Min Lin Diecast",
        "quantityInStock": "7933"
    }
    :return: 'Success' if no errors occur, but it's now lack of error handling.
    """
    productRepo = ProductRepo()
    productRepo.create_new(request.json)
    return 'Success'

