# my practice OOP

class Person:

    def __init__(self, name, age, children):
        self.name = name
        self.age = age
        self.children = children

    def get_info(self):
        info = {'Name': self.name, 'Age': self.age, 'Children': self.children}
        return info


human = Person('Denis', 30, 'Not')
for k, v in human.get_info().items():
    print(f'{k}: {v}')       