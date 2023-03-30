from abc import ABC, abstractmethod

class System:
    def __init__(self):
        pass
    def call_scraper():
        pass


class Scraper:
    def __init__(self):
        pass
    def scrap():
        pass


class Information:
    def __init__(self, list_p=[], list_s=[]):
        self.list_p= list_p
        self.list_s= list_s
        
    def create_movie():
        pass
    def create_serie():
        pass


class Peliculas:
    def __init__(self) -> None:
        pass

    def filter_gender():
        pass


class Series:
    def __init__(self) -> None:
        pass

    def filter_gender():
        pass


class User(ABC):
    def __init__(self, name, age, list_p_f=[], list_s_f=[]):
        self.name= name
        self.age=age
        self.list_p_f= list_p_f
        self.list_s_f= list_s_f
    
    @abstractmethod
    def watch_movie():
        pass
    @abstractmethod
    def watch_serie():
        pass
    def recommend():
        pass
    def rate():
        pass
    def add_fav():
        pass
    def value_age():
        pass


class AdultUser(User):
    def __init__(self, nombre, edad, list_p_f=[], list_s_f=[]):
        super().__init__(nombre, edad, list_p_f, list_s_f)

    def watch_movie():
        pass
    def watch_serie():
        pass

class MinorUser(User):
    def __init__(self, nombre, edad, list_p_f=[], list_s_f=[]):
        super().__init__(nombre, edad, list_p_f, list_s_f)
    
    def watch_movie():
        pass
    def watch_serie():
        pass


        
