from PIL import Image
import numpy as np

def ft_load(path: str) -> list:
    img = Image.open(path)
    #img.show()

    print("Format:", img.size)