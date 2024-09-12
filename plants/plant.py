class Plant:
    def __init__(self, name, height, type):
        self.name = name
        self.height = height
        self.type = type

    def display_info(self):
        return f"Plant Name: {self.name}, Height: {self.height} cm, Type: {self.type}"

    def grow(self, growth):
        self.height += growth
        return f"New Height after growing {growth} cm: {self.height} cm"

# Example usage
plant1 = Plant("Rose", 30, "Flowering")
print(plant1.display_info())
print(plant1.grow(10))
