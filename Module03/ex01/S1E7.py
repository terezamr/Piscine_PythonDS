from S1E9 import Character

class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, name, health=True, family_name="Baratheon", eyes='brown', hairs='dark'): # called automatically to create a new obj
        """Init method"""
        super().__init__(name, health)
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs
    
    def die(self):
        """Die method"""
        self.is_alive = False
    
    def __str__(self):
        return f'Vector: ({self.family_name}, {self.hairs}, {self.eyes})'

    def __repr__(self):
        return f'Vector: ({self.family_name}, {self.hairs}, {self.eyes})'

class Lannister(Character):
    """Representing the Lannister family."""
    def __init__(self, name, health=True, family_name="Lannister", eyes='blue', hairs='light'): # called automatically to create a new obj
        """Init method"""
        super().__init__(name, health)
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs
    
    def die(self):
        """Die method"""
        self.is_alive = False
    
    def __str__(self):
        return f'Vector: ({self.family_name}, {self.hairs}, {self.eyes})'

    def __repr__(self):
        return f'Vector: ({self.family_name}, {self.hairs}, {self.eyes})'

    # class method can be used as a factory method to get an object of the class
    @classmethod
    def create_lannister(cls, name, health): # cls - used to acess class attributes
        return cls(name, health)