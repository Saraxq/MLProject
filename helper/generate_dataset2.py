import os

import cv2
import numpy as np

path_to_files = "../mydataset/images/face_images/"
images = []
labels = []
for image in os.listdir(path_to_files):
    label = int(image[0: 1])
    image = os.path.join(path_to_files, image)
    image = cv2.imread(image, cv2.IMREAD_COLOR)
    # i = cv2.imread(i, cv2.IMREAD_GRAYSCALE)
    # cv2.resize(image, (96, 96, 7049))
    images.append(image)
    labels.append(label)

images = np.asarray(images)
labels = np.asarray(labels)

# arr_path = "some/path"
# np.save("../mydataset/new/images.npy", images)
# np.save("../mydataset/new/labels.npy", labels)

# or optionally
np.savez("../mydataset/new/dataset.npz", images, labels)