import zipfile
import numpy as np


def read_metadata(file_name):
    zip_file = zipfile.ZipFile(file_name, mode='r')
    arr_names = zip_file.namelist()

    metadata = []
    for arr_name in arr_names:
        fp = zip_file.open(arr_name, "r")
        version = np.lib.format.read_magic(fp)

        if version[0] == 1:
            shape, fortran_order, dtype = np.lib.format.read_array_header_1_0(fp)
        elif version[0] == 2:
            shape, fortran_order, dtype = np.lib.format.read_array_header_2_0(fp)
        else:
            print("File format not detected!")
        metadata.append((arr_name, shape, fortran_order, dtype))
        fp.close()
    zip_file.close()
    return metadata


print(read_metadata('../dataset/facelandmark/face_images.npz'))

print(read_metadata('../mydataset/new/dataset.npz'))

