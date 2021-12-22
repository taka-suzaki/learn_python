class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
class Dog(Animal):
    pass

class Cat(Animal):
    pass


if __name__ == "__main__":
    dog = Dog('pochi', 3)
    cat = Cat('tama', 5)
    
    print(type(dog), type(cat))
    print(isinstance(dog, Animal))
    print(isinstance(dog, Dog))