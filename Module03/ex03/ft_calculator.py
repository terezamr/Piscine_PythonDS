class calculator:
    def __init__(self, vector):
        """Init method"""
        self.v = vector

    def __add__(self, object) -> None:
        self.v = [x + object for x in self.v]
        print(self.v)

    def __mul__(self, object) -> None:
        self.v = [x * object for x in self.v]
        print(self.v)

    def __sub__(self, object) -> None:
        self.v = [x - object for x in self.v]

        print(self.v)

    def __truediv__(self, object) -> None:
        if object == 0:
            print('Error')
            return 
        self.v = [x / object for x in self.v]
        print(self.v)