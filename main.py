# my practice OOP

class Person:

    def __init__(self, name=None, lastname=None, age=None, kids=None, job=None, adress=None, profession=None):
        self.name = name
        self.last_name = lastname
        self.age = age
        self.kids = kids
        self.job = job
        self.adress = adress
        self.profession = profession

    # функция для возврата информации о человеке
    def get_info(self):
        info = {'Name': self.name, 'lastname': self.last_name, 'Age': self.age, 'Kids': self.kids, 
                'job': self.job, 'adress': self.adress, 'profession': self.profession}
        return info
    
    # функция для добавления или изменения имени человека
    def set_name(self, name):
        if type(name) is str:
            self.name = name
        else:
            raise ValueError('Введены неккоректные данные')

    # функция для добавления или изменения  фамилии человека
    def set_last_name(self, last_name):
        if type(last_name) is str:  
            self.last_name = last_name
        else:
            raise ValueError('Введены неккоректные данные')

    # функция для добавления или изменения фамилии человека
    def set_age(self, age):
        if type(age) is int:
            self.age = age
        else:
            raise ValueError('Введены неккоректные данные')

    # функция для добавления детей
    def add_chield(self, chield):
        if self.kids is None:
            self.kids = []
        self.kids.append(chield)
    
    # функция для добавления или изменения адреса
    def set_adress(self, adress):
        self.adress = adress


    # функция для добавления или изменения места работы человека
    def set_job(self, job):
        self.job = job


    # функция для добавления или изменения профессии человека
    def set_profession(self, profession):
        self.profession = profession
    




    
 


