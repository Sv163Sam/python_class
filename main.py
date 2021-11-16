# This is a sample Python script.c
import argparse
#parser = argparse.ArgumentParser()
#parser.add_argument('100.txt', help="Название файла, с которого считаываются данные")
#parser.add_argument('300.txt', help="Названия файла, куда сохранятся валидные данные")
#args = parser.parse_args()



from tqdm import tqdm
from validator import validate, Pattern, GreaterThan

import json
import re

path = '/Users/vladimirskobcov/PycharmProjects/pythonProject/100.txt'
data = json.load(open(path, encoding='windows-1251'))

list1 = []
for line in data:
    list1.append(str(line))


class Peoples:
    def __init__(self, telephone: str, height: str, snils: str, passport_series: str, university: str, work_experience: str, political_views: str, worldview: str, address: str) -> None:
        self.__telephone = telephone
        self.__height = height
        self.__snils = snils
        self.__passport_series = passport_series
        self.__university = university
        self.__work_experience = work_experience
        self.__political_views = political_views
        self.__worldview = worldview
        self.__address = address

    #
    #
    # THE Class Peoples - Describe properties, that we read from the file through data fields
    #
    #

    @property
    def get_telephone(self):
        return self.__telephone

    @property
    def get_height(self):
        return self.__height

    @property
    def get_snils(self):
        return self.__snils

    @property
    def get_passport(self):
        return self.__passport_series

    @property
    def get_university(self):
        return self.__university

    @property
    def get_work(self):
        return self.__work_experience

    @property
    def get_political(self):
        return self.__political_views

    @property
    def get_worldview(self):
        return self.__worldview

    @property
    def get_address(self):
        return self.__address

    #GETTERS - Methods(), that allow us to get data from one of all fields

    def display_info(self) -> str:
        print(self.__telephone, self.__height, self.__snils, self.__passport_series,
              self.__university, self.__work_experience, self.__political_views, self.__worldview, self.__address)

    #This method displays all information about one person on the screen.

with tqdm(total=len(list1)) as progressbar:
    for count in range(len(list1)):
        d = eval(list1[count])
        person1 = Peoples(d['telephone'], d['height'], d['snils'], d['passport_series'], d['university'], d['work_experience'], d['political_views'], d['worldview'], d['address'])
        #Regular Expression Validation Criteries
        telephone = {
            "telephone": person1.get_telephone
        }
        validation_telephone = {
            "telephone": [Pattern("\+\d\-\(\d\d\d\)\-\d\d\d\-\d\d\-\d\d")]
        }
        height = {
            "height": person1.get_height
        }
        validation_height = {
            "height": [Pattern("\d\.\d\d")]
        }
        snils = {
            "snils": person1.get_snils
        }
        validation_snils = {
            "snils": [Pattern("\d\d\d\d\d\d\d\d\d\d\d")]
        }
        passport_series = {
            "passport_series": person1.get_passport
        }
        validation_passport_series = {
            "passport_series": [Pattern("\d\d\ \d\d")]
        }
        university = {
            "university": person1.get_university
        }
        validation_university = {
            "university": [Pattern("[А-Яа-я]+")]
        }
        work_experience = {
            "work_experience": person1.get_work
        }
        validation_work_experience = {
            "work_experience": [GreaterThan(17)]
        }
        political_views = {
            "political_views": person1.get_political
        }
        validation_political_views = {
            "political_views": [Pattern("[А-Яа-я]+")]
        }
        worldview = {
            "worldview": person1.get_worldview
        }
        validation_worldview = {
            "worldview": [Pattern("[А-Яа-я]{0,15}")]
        }
        address = {
            "address": person1.get_address
        }
        validation_address = {
            "address": [Pattern("[А-Яа-я]{0,45}[0-9]{0,7}")]
        }
        path1 = "/Users/vladimirskobcov/PycharmProjects/pythonProject/300.txt"
        def write(list):
            f = open(path1, "w")
            f.write("\n"+list)
            f.close()
        #VALIDATION PROCCES AND CHECK VALID DATA
        if (validate(validation_telephone, telephone) == (True, {})):
            if (validate(validation_height, height) == (True, {})):
                if(validate(validation_snils, snils) == (True, {})):
                    if(validate(validation_passport_series, passport_series) == (True, {})):
                        if(validate(validation_work_experience, work_experience) == (True, {})):
                            if(validate(validation_worldview, worldview) == (True, {})):
                                if (validate(validation_university, university) == (True, {})):
                                    if(validate(validation_address, address) == (True, {})):
                                        if(validate(validation_political_views, political_views) == (True, {})):
                                            write(str(list1))
                                            print(list1[count])
        progressbar.update(1)
        del person1