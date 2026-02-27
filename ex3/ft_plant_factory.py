class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        return f"{self.name}: {self.height}cm, {self.age} days old"


plant1 = Plant("Rose", 25, 30)
plant2 = Plant("Oak", 200, 365)
plant3 = Plant("Cactus", 90, 120)
plant4 = Plant("Sunflower", 80, 45)
plant5 = Plant("Fern", 15, 120)

print("=== Plant Factory Output ===")

for plant in [plant1, plant2, plant3, plant4, plant5]:
    print(f"Created: {plant.name} ({plant.height}cm, {plant.age} days)")

print("\nTotal plants created: 5")
