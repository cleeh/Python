class Animal:
    def cry(self):
        print("/./././.")
class Human(Animal):
    def cry(self):
        print('EaongEaong')
class Whale(Animal):
    def cry(self):
        print('Gguang')
class Monkey(Animal):
    def cry(self):
        print('Ukiki')
for instance in (Human(), Whale(), Monkey()):
    instance.cry()