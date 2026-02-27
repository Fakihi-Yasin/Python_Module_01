class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


p1 = Plant("Rose", 25, 30)
p2 = Plant("Sunflower", 85, 45)
p3 = Plant("Cactus", 15, 120)


print("=== Garden Plant Registry ===")
for plant in [p1, p2, p3]:
    print(f"{plant.name}: {plant.height}cm, {plant.age} days old")
