from PIL import Image
import numpy as np

def ft_load(path: str) -> np.array:
    try:
        x = path.split(".")
        if x[1] != "jpg" and x[1] != "jpeg":
            raise ValueError("Wrong picture format")

        img = Image.open(path) 
        px = np.array(img)
        print("Format:", px.shape)
        return px
    except ValueError as e:
        print("Error: ", e)
    except:
        print("Error",)