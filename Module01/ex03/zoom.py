from load_image import ft_load
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def zoom(img_array: np.array):
    print(img_array)

    plt.xlim((100,200))
    plt.ylim((25,150))
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.imshow(img_array) # draws an image on the current figure
    plt.gca().invert_yaxis()
    plt.show() #displays figure

    zoomed_img = img_array[int(100):int(300), int(220):int(420)]
    px = np.array(zoomed_img)
    print("New shape after slicing: ", px.shape, "\n", px)

def main():
    zoom(ft_load("landscape.jpg"))

if __name__ == "__main__":
    main()
