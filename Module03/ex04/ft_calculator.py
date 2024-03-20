import numpy as np

# decorator - expression that gets evaluated after the function is defined

class calculator:
    def __init__(self):
        """Init method"""
    
    @staticmethod # cant modify the class, used for utility functions
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        result = np.dot(V1, V2)
        print("Dot product is:", result)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        result = [float (x + y) for x, y in zip(V1, V2)]
        print("Add Vector is:", result)

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        result = [float(x - y) for x, y in zip(V1, V2)]
        print("Sous Vector is:", result)