class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.energy = 100


def birthday(self):
    self.age += 1
    print(f"{self.name} 'Cat had birthday party!'")


def played(self):
    if self.energy >= 15:
        self.energy -= 15
        print(f"{self.name} Cat has palayed with string {self.energy}")