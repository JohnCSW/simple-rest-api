from entity.product import Product
from repo.base_repo import BaseRepo


class ProductRepo(BaseRepo):
    def __init__(self):
        super().__init__()

    def create_new(self, data):
        product = Product(
            productCode=data['productCode'],
            productName=data['productName'],
            productLine=data['productLine'],
            productScale=data['productScale'],
            productVendor=data['productVendor'],
            productDescription=data['productDescription'],
            quantityInStock=data['quantityInStock'],
            buyPrice=data['buyPrice'],
            MSRP=data['MSRP']
        )
        # TODO: Error Handling
        self.session.add(product)
        return self.session.commit()
