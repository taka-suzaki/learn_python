class Animal:
    def __init__(self, name, age, kind='', **kwargs):
        print(kwargs)
        self.name = name
        self.age = age
        self.kind = kind
        
        self.lis = {}
        
    def set_name(self, name):
        
        self.lis = {"name": self.name}
        t = {"a": self.lis}
        print(t)
        self.lis = dict()
        print(t)
        
class Dog(Animal):
    pass

class Cat(Animal):
    pass


if __name__ == "__main__":
    animal = Animal('a', 0)
    kwargs = {
        'name': 'pochi',
        'age': 3,
        'kind': 'shiba',
        'color': 'black'
    }
    dog = Dog(**kwargs)
    dog.set_name("jiro")
    # cat = Cat('tama', 5)
    
    # print(type(dog), type(cat))
    print(isinstance(Dog, Animal), isinstance(dog, Dog))
    print(issubclass(Dog, Animal))
    
    # print(dog.kind)
    
    