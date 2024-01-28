class Dog():
    def __init__(self, class_name):
        self.class_name = class_name

    def get_name(name):
        print(name)

class Cat():
    def __init__(self, class_name):
        self.class_name = class_name

    def get_name(name):
        print(name)

class Fish():
    def __init__(self, class_name):
        self.class_name = class_name

    def get_name(name):
        print(name)

class Lion():
    def __init__(self, class_name):
        self.class_name = class_name

    def get_name(name):
        print(name)

class Python():
    def __init__(self, class_name):
        self.class_name = class_name

    def get_name(name):
        print(name)

class Animal():
    dog = Dog
    cat = Cat
    fish = Fish
    lion = Lion
    python = Python

class_name = 'cat'
name = 'Cute'

obj = getattr(Animal,class_name)(name)
print(obj.class_name)