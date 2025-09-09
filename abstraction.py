from abc import ABC, abstractmethod

class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class car(vehicle):
    def start(self):
        return "car has started"
    
    def stop(self):
        return "car has stoped"

class bike(vehicle):
    def start(self):
        return "bike has started"

s1=car()
s2=bike()
print(s1.start())
print(s1.stop())
print(s2.start())
