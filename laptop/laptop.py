class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_info(self):
        return f"Laptop Brand: {self.brand}, Model: {self.model}, Price: ${self.price}"

    def apply_discount(self, discount):
        self.price -= self.price * (discount / 100)
        return f"New Price after {discount}% discount: ${self.price}"

# Example usage
laptop1 = Laptop("Dell", "XPS 13", 1200)
print(laptop1.display_info())
print(laptop1.apply_discount(10))
