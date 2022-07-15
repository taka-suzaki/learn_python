from torch import ge


class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            print(self.name, *args, **kwargs)
            
        return wrapper
    
    @decorator
    def show(self, num):
        print(num)


class Child(Parent):
    def __init__(self, name, age):
        super(self).__init__(name, age)
    
    @decorator
    def show(self, num):
        print("child", num)
        

if __name__ == '__main__':
    parent = Parent("taro", 32)
    child = Child("kojiro", 6)
    
    parent.show()
    child.show()