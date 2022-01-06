import os
from PIL import Image
import numpy as np

image_root_dirs = ["1", "2", "3"]
crop_dir = "crop"
concatenated_dir = "concatenated"

if not os.path.exists(concatenated_dir):
    os.mkdir(concatenated_dir)

file_types = ['.jpg', '.bmp', '.jpeg', '.gif', '.img', '.png', '.tiff', '.tif', ".npy"]

image_list = []
for dir in image_root_dirs:
    image_dir = os.path.join(dir, crop_dir)
    list_of_files = []
    for file in os.listdir(image_dir):
        filename, extention = os.path.splitext(file)
        if extention in file_types:
            list_of_files.append(os.path.join(image_dir, file))
    image_list.append(list_of_files)

min_length = len(min(image_list, key=len))

def convert_2Darray(img_path):
    img_array = np.load(img_path)
    img_shape = img_array.shape
    if len(img_shape) > 2:
        img_array = np.squeeze(img_array, axis=2)
    return img_array

for index in range(min_length):
    first_image = image_list[0][index]
    second_image = image_list[1][index]
    third_image = image_list[2][index]
    r = convert_2Darray(first_image)
    g = convert_2Darray(second_image)
    b = convert_2Darray(third_image)
    combined = np.dstack((r, g, b))
    save_path = os.path.join(concatenated_dir, str(index) + ".npy")
    np.save(save_path, combined)
    
