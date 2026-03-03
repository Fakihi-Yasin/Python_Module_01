class SecurePlant:

    def __init__(self, name: str, height: int, age: int) -> None:

        self.name = name
        self.__height = height
        self.__age = age

    def set_height(self, height: int) -> None:

        if (height < 0):
            print(f"Invalid operation attempted: height {height} cm [REJECTED]"
                  f".\nSecurity: Negative height rejected\n")
        else:
            self.__height = height
            print(f"Height updated: {self.get_height()}cm [OK]")

    def get_height(self) -> int:

        return self.__height

    def set_age(self, age: int) -> None:

        if (age < 0):
            print(f"Invalid operation attempted: age {age} days [REJECTED]"
                  f".\nSecurity: Negative age rejected\n")
        else:
            self.__age = age
            print(f"Age updated: {self.get_age()} days [OK]")

    def get_age(self) -> int:

        return self.__age


plant1 = SecurePlant("rose", 10, 5)

print("=== Garden Security System ===")
print("Plant created: " + plant1.name)
plant1.set_height(-5)
plant1.set_age(30)
print(f"\nCurrent plant: {plant1.name} ({plant1.get_height()}"
      f"cm, {plant1.get_age()} days)")
