class Train:
    def __init__(self, name, speed, capacity):
        self.name = name
        self.speed = speed
        self.capacity = capacity

    def display_info(self):
        return f"Train Name: {self.name}, Speed: {self.speed} km/h, Capacity: {self.capacity} passengers"

    def update_speed(self, new_speed):
        self.speed = new_speed
        return f"Updated Speed: {self.speed} km/h"

# Example usage
train1 = Train("Bullet Train", 300, 1000)
print(train1.display_info())
print(train1.update_speed(320))
