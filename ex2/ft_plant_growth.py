class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        self.height += 1

    def age_up(self):
        self.age += 1

    def get_info(self):
        return f"{self.name}: {self.height}cm, {self.age} days old"


rose = Plant("Rose", 25, 30)

initial_height = rose.height

print("=== Day 1 ===")
print(rose.get_info())

for day in range(6):
    rose.grow()
    rose.age_up()

print("=== Day 7 ===")
print(rose.get_info())
print(f"Growth this week: {rose.height - initial_height}cm")
