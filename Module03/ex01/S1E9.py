from abc import ABC, abstractmethod

# A class with one or more abstract methods is an abstract class
# provides common interface for different implementations
# abstract method - declaration but no implementation

class Character(ABC):
    """Character Class"""
    def __init__(self, name, health=True): # called automatically to create a new obj
        """Init method"""
        self.first_name = name
        self.is_alive = health
    
    @abstractmethod
    def die(self):
        pass

class Stark(Character):
    """stark Class"""
    def die(self):
        """Die method"""
        self.is_alive = False 