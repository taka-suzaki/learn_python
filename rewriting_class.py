class A:
    def __init__(self, name):
        self.name = name
        self.kind = 'a'
        
    def run():
        print("oraaaaaa")

class B:
    def __init__(self, name):
        self.name = name
        self.kind = 'b'
        
        
    def run():
        print("kyaaaaaaaaaaa")
        
        
class Copy:
    def __init__(self, kind):
        if kind == 'a':
            obj = A('a_copy')
        elif kind == 'b':
            obj = B('b_copy')
        
        self.__class__ = obj.__class__
        self.__dict__ = obj.__dict__
        # self.__module__ = obj.__module__
        self.kind = 'copy'
        

if __name__ == '__main__':
    copy = Copy('a')
    print(copy)
    print(type(copy) is A)
    print(copy.name, copy.kind)
    copy.run()
    