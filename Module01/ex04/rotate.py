from load_image import ft_load
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def zoom(img_array: np.array) -> np.array:
    plt.xlim((100,200))
    plt.ylim((0,100))
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.imshow(img_array) # draws an image on the current figure
    plt.gca().invert_yaxis()
    plt.show() #displays figure

    zoomed_img = img_array[int(100):int(300), int(220):int(420)]
    px = np.array(zoomed_img)
    return px

def rotate(img_array: np.array):
    plt.imshow(img_array)
    plt.show()
    print("The shape of the image is: ", img_array.shape)

    zoomed = zoom(img_array)
    plt.show()
    print("New shape after zoom: ", zoomed.shape)

    zoomed_d = np.delete(zoomed, [1, 2], 2)
    print("New shape after delete col: ", zoomed_d.shape)
    zoomed_t = np.transpose(zoomed_d)
    print("New shape after Transpose: ", zoomed_t.shape)
    print("new\n", zoomed_t)
    #plt.imshow(zoomed_t)
    #plt.show()

def main():
    rotate(ft_load("images.jpeg"))

if __name__ == "__main__":
    main()
