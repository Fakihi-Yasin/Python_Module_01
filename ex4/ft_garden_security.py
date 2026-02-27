class SecurePlant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def set_height(self, height):
        if (height < 0):
            print(f"Invalid operation attempted: height {height}cm [REJECTED]"
                  f".\nSecurity: Negative height rejected\n")
        else:
            self.height = height
            print(f"Height updated:{self.get_height()}cm [OK]")

    def get_height(self):
        return self.height

    def set_age(self, age):
        if (age < 0):
            print(f"Invalid operation attempted: age {age} days [REJECTED]"
                  f".\nSecurity: Negative age rejected\n")
        else:
            self.age = age
            print(f"Age updated: {self.get_age()} days [OK]")

    def get_age(self):
        return self.age


plant1 = SecurePlant("rose", 10, 5)

print("=== Garden Security System ===")
print("Plant created: " + plant1.name)
plant1.set_height(25)
plant1.set_age(30)
plant1.set_height(-5)
print(f"\nCurrent plant: {plant1.name} ({plant1.get_height()}"
      f"cm, {plant1.get_age()} days)")
