class Person:
    def __init__(self, name, gender, age, origin, destination, mood):
        self.__name = name
        self.__gender = gender
        self.__age = age
        self.__origin = origin
        self.__destination = destination
        self.__mood = mood

    def get_name(self):
        return self.__name
    
    def get_pronouns(self):
        return self.__pronoun
    
    def get_age(self):
        return self.__age

    def get_origin(self):
        return self.__origin
    
    def get_destination(self):
        return self.__destination
    
    def get_mood(self):
        return self.__mood

    def get_gender(self):
        return self.__gender

