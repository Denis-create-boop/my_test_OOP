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


    # function for return person's info
    def get_info(self):
        info = {'gender': self.gender, 'Name': self.name, 'lastname': self.last_name, 'Age': self.age, 
                'Kids': self.kids, 'job': self.job, 'adress': self.adress, 'profession': self.profession}
        return info
    

    # function for change or add person's name
    def set_name(self, name):
        if type(name) is str:
            self.name = name
        else:
            raise ValueError('Введены неккоректные данные')


    # function for change or add person's last name
    def set_last_name(self, last_name):
        if type(last_name) is str:  
            self.last_name = last_name
        else:
            raise ValueError('Введены неккоректные данные')


    # fuvction for change or add person's age
    def set_age(self, age):
        if type(age) is int:
            self.age = age
        else:
            raise ValueError('Введены неккоректные данные')


    # function for add person's kids
    def add_chield(self, chield):
        if self.kids is None:
            self.kids = []
        self.kids.append(chield)
    

    # function for chenge or add person's adress
    def set_adress(self, adress):
        self.adress = adress


    # function for change or add person's job
    def set_job(self, job):
        self.job = job


    # function for change or add person's prfession
    def set_profession(self, profession):
        self.profession = profession
    

    # function for change or set person's gender
    def set_gender(self, gender):
        if gender.lower() in ['мужской', 'женский', 'male', 'female']:
            self.gender = gender
        else:
            raise ValueError('Введены неккоректные данные')

    
 
# create class Woecker and inherited from class Person
class Worcker(Person):
    """класс для представления, создания или изменения информации о работнике"""
    def __init__(self, post=None, salery=None, expirience=None, level=None):
        super().__init__(name=None, lastname=None, age=None, gender=None, kids=None, job=None, adress=None, 
                        profession=None)
        self.post = post
        self.salery = salery
        self.expirience = expirience
        self.level = level

    # function for return information about worcker
    def show_info(self):
        info = {'name': self.name, 'lastname': self.last_name, 'age': self.age, 'gender': self.gender, 
                'kids': self.kids, 'job': self.job, 'adress': self.adress, 'profession': self.profession, 
                'post': self.post, 'salery': self.salery, 'expirience': self.expirience, 'level': self.level}
        return info


    # function for change or add worcker's post
    def set_post(self, post):
        self.post = post

    # function for change or add worcker's salery
    def set_salery(self, salery):
        if type(salery) is int or type(salery) is float:
            self.salery = salery
        else:
            raise ValueError('ВВедите число')

    # function for change or add worcker's expirience
    def set_expirience(self, expirience):
        self.expirience = expirience

    # function for change or add worckwe's level
    def set_level(self, level):
        self.level = level




per = Worcker('denis', 'Glone', '25', 'male')

print(per.show_info())