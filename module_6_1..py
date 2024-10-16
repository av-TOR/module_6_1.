class Animal:
    def __init__(self,name,  alive=True, fed=False):
        self.name = name
        self.alive = alive
        self.fed = fed


class Plant:
    def __init__(self, name, edible=False):
        self.name = name
        self.edible = edible


class Mammal(Animal):

    def eat(self, food):
        if food.edible == True:
            print(f"{self.name} съел {food.name}")
            self.fed = True

        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False


class Predator(Animal):

    def eat(self, food):
        if food.edible == True:
            print(f"{self.name} съел {food.name}")
            self.fed = True

        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False


class Flower(Plant):
    pass


class Fruit (Plant):
    def __init__(self, name, edible=True):
        super().__init__(name)
        self.edible = edible


Fox = Predator('Лиса')
Dog = Mammal('Маламут')
Mak = Flower('Мак')
Apple = Fruit('Яблоко')

print(Fox.name)
print(Mak.name)
print(Fox.alive)
print(Dog.fed)

Fox.eat(Mak)
Dog.eat(Apple)

print(Fox.alive)
print(Dog.fed)

