# my practice OOP

from httpx import post


class Person:
    """класс для создания персоны 'человек', также для изменения и хранения информации о конкретном человеке"""
    def __init__(self, name=None, lastname=None, age=None, gender=None, kids=None, job=None, adress=None, 
                 profession=None):
        self.name = name
        self.last_name = lastname
        self.age = age
        self.kids = kids
        self.gender = gender
        self.job = job
        self.adress = adress
        self.profession = profession


    # функция для возврата информации о человеке
    def get_info(self):
        info = {'gender': self.gender, 'Name': self.name, 'lastname': self.last_name, 'Age': self.age, 
                'Kids': self.kids, 'job': self.job, 'adress': self.adress, 'profession': self.profession}
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
    

    # функция для установки или изменения пола человека
    def set_gender(self, gender):
        if gender.lower() in ['мужской', 'женский', 'male', 'female']:
            self.gender = gender
        else:
            raise ValueError('Введены неккоректные данные')

    
 
# создаем класс работник(Worcker) и наследуемся от класса персона(Person)
class Worcker(Person):
    """класс для представления, создания или изменения информации о работнике"""
    def __init__(self, post=None, salery=None, expirience=None, level=None):
        super.__init__(name=None, lastname=None, age=None, gender=None, kids=None, job=None, adress=None, 
                        profession=None)
        self.post = post
        self.salery = salery
        self.expirience = expirience
        self.level = level


    def show_info(self):
        pass


    # функция для изменения или добавления должности сотрудника
    def set_post(self, post):
        self.post = post


    def set_salery(self, salery):
        pass


    def set_expirience(self, expirience):
        pass


    def set_level(self, level):
        pass