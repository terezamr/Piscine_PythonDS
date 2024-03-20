from S1E7 import Baratheon, Lannister

class King(Baratheon, Lannister):
    '''The King'''
    def get_eyes(self):
        return self.eyes

    def get_hairs(self):
        return self.hairs

    def set_eyes(self, str):
        self.eyes = str

    def set_hairs(self, str):
        self.hairs = str