class Category:
    categories_count = 0
    unique_products_count = 0

    def __init__(self, name:str, description:str, products:list = None):
        self.name = name
        self.description = description
        self.products = products if products is not None else []
        Category.categories_count += 1
        Category.unique_products_count += len(self.products)

    # def __repr__(self):
    #     return f'name={self.name}, description={self.description}, products={self.products}'


class Product:
    def __init__(self, name: str, description : str, price: float, in_stock: int):
        self.name = name
        self.description = description
        self.price = price
        self.in_stock = in_stock


    # def __repr__(self):
    #     return self.name, self.description