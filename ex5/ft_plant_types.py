class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        print(f"{self.name} provides 78 square meters of shade")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):

        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value


flower1 = Flower("Rose", 25, 30, "red")
flower2 = Flower("Tulip", 40, 1, "yellow")

tree1 = Tree("Oak", 500, 1825, 50)
tree2 = Tree("Pine", 300, 1095, 30)

vegetable1 = Vegetable("Tomato", 80, 90, "summer", "rich in vitamin C")
vegetable2 = Vegetable("Carrot", 60, 120, "fall", "high in beta-carotene")

print("=== Garden Plant Types ===")
print(f"\n{flower1.name} (Flower): {flower1.height}cm, {flower1.age} days"
      f", {flower1.color} color")

flower1.bloom()
print(f"\n{tree1.name} (Tree): {tree1.height}cm, {tree1.age} days"
      f", {tree1.trunk_diameter}cm diameter")

tree1.produce_shade()
print(f"\n{vegetable1.name} (Vegetable): {vegetable1.height}cm"
      f", {vegetable1.age} days, {vegetable1.harvest_season} harvest")

print(f"{vegetable1.name} is {vegetable1.nutritional_value}")
