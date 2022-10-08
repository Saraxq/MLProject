# generate and save file
from PIL import Image
import os
import numpy as np

path_to_files = "../mydataset/images/face_images/"
vectorized_images = []

for _, file in enumerate(os.listdir(path_to_files)):
    image = Image.open(path_to_files + file)
image_array = np.array(image)
vectorized_images.append(image_array)

np.savez("../mydataset/new/my-images.npz", data_images=vectorized_images)
