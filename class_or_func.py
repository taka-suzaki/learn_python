import inspect

class A:
    def __init__(self):
        pass
    
    def __call__(self):
        pass
    
    def f(self, x):
        pass

def func():
    pass


if __name__ == "__main__":
    print("A func?", callable(A))
    print("A() func?", callable(A()))
    print("A().f func?", callable(A().f))
    print("func is func?", callable(func))
    print("A class?", inspect.isclass(A))
    print("A() class?", inspect.isclass(A()))
    print("func class?", inspect.isclass(func))