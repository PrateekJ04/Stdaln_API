# 2.Abstraction
from abc import ABC, abstractmethod


# If any abstract method is present in class then programm will not get executed until abstract method is completed
class New_Abstract(ABC):
    def name_of_bike(self):
        print("You have purchased Ducati Panigale")

    @abstractmethod
    def color_of_bike(self):
        print("What color do you have for the bike")


# Here we have abstract method is completed
class making_abstract_complete(New_Abstract):
    def color_of_bike(self):
        print("What color do you have for the bike?")
        print("I have model of Ducati in Black")


a = making_abstract_complete()
a.name_of_bike()
a.color_of_bike()
