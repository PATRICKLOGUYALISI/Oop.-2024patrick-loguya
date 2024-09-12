class Fan:
    def __init__(self, brand, speed_levels, price):
        self.brand = brand
        self.speed_levels = speed_levels
        self.price = price

    def display_info(self):
        return f"Fan Brand: {self.brand}, Speed Levels: {self.speed_levels}, Price: ${self.price}"

    def change_speed(self, level):
        if 1 <= level <= self.speed_levels:
            return f"Fan speed set to level {level}"
        else:
            return "Invalid speed level"

# Example usage
fan1 = Fan("Panasonic", 5, 50)
print(fan1.display_info())
print(fan1.change_speed(3))
