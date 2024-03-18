from load_image import ft_load
from PIL import Image
import numpy as np

import matplotlib.pyplot as plt
#from imageio import imread
#import SimpleITK as sitk
#import fetch_data as fdata


def main():
    img = np.array("landscape.jpg")
    # display data as am image
    plt.imshow(img)
    #plt.show()

if __name__ == "__main__":
    main()