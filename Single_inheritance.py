class Product:
    def __init__(self, name, price, brand, warranty):
        self.name = name
        self.price = price
        self.brand = brand
        self.warranty = warranty

    def display(self):
        print("Product Name:", self.name)
        print("Product Price:", self.price)
        print("Product Brand:", self.brand)
        print("Warranty:", self.warranty, "years")

    def calc_price(self, count):
        total = self.price * count
        print("Total price:", total)


class Electronics(Product):
    def __init__(self, name, price, brand, warranty):
        super().__init__(name, price, brand, warranty)
        self.type = "Electronics"

    def displayall(self):
        super().display()
        print("Product Type:", self.type)

e1 = Electronics("Laptop", 50000, "Dell", 2)

e1.displayall()

e1.calc_price(3)
