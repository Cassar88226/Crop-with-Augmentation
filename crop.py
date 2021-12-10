import os
import numpy as np
import glob
from PIL import Image
mask_root_dir = "./4"
image_root_dirs = ["./1", "./2", "./3"]

output_dir = "output"
crop_dir = "crop"
file_types = ['*.jpg', '*.bmp', '*.jpeg', '*.gif', '*.img', '*.png', '*.tiff', '*.tif', "*.npy"]

class PillImage(object):
    def __init__(self, file, file_format = None, file_type = None):
        self.file = file
        self.file_format = file_format
        self.file_type = file_type
        self.depth = None
        self.image = None
    def get_file_formt(self):
        return os.path.splitext(self.file)[1].split(".")[1]

    def get_image(self, raw_type = False):
        self.file_format = self.get_file_formt()
        if self.file_format != "npy":
            img = Image.open(self.file)
            self.image = img
            return img, img.size
        else:
            img_array = np.load(self.file)
            self.file_type = img_array.dtype
            img_shape = img_array.shape
            if len(img_shape) > 2:
                img_array = np.squeeze(img_array, axis=2)
                self.depth = img_shape[2]
            if not raw_type:                
                formatted = ((img_array - np.min(img_array)) * 255 / (np.max(img_array) - np.min(img_array))).astype('uint8')
                img = Image.fromarray(formatted)
                self.image = img
                return img, img.size
            else:
                self.image = img_array
                return img_array, (img_shape[1], img_shape[0])

    def get_bbox(self):
        img, _ = self.get_image()
        bbox = img.convert('RGB').getbbox()
        return bbox
    def crop(self, bbox):
        if self.file_format != "npy":
            return self.image.crop(bbox)
        else:
            return self.image[bbox[1] : bbox[3], bbox[0] : bbox[2]]
            
    def save_image(self, image, save_path):
        if self.file_format == "npy":
            # normal_img = np.asarray(image) / 255
            # if self.file_type == "float32":
            #     normal_img = np.float32(normal_img)
            # elif self.file_type == "float64":
            #     normal_img = np.float64(normal_img)
            # else:
            #     normal_img = np.uint8(normal_img)
            if self.depth is not None:
                image = np.reshape(image, (image.shape[0], image.shape[1], self.depth))
            np.save(save_path, image)
        else:
            image.save(save_path)


def valid_bbox(size, bbox):
    width = bbox[2] - bbox[0]
    height = bbox[3] - bbox[1]
    return width <= size[0] and height <= size[1]

def crop_dir_images(dir, bbox):
    image_dir = os.path.join(dir, output_dir)
    list_of_files = os.listdir(image_dir)
    if basename in list_of_files and bbox is not None:
        pil_img = PillImage(os.path.join(image_dir, basename))            
        img, size = pil_img.get_image(raw_type=True)
        if valid_bbox(size, bbox):
            cropped_img = pil_img.crop(bbox)
            save_dir = os.path.join(dir, crop_dir)
            if not os.path.exists(save_dir):
                os.mkdir(save_dir)
            pil_img.save_image(cropped_img, os.path.join(save_dir, basename))
# get list of image files
list_of_mask_files = []

mask_directory = os.path.join(mask_root_dir, output_dir)
for file_type in file_types:
    list_of_mask_files.extend(glob.glob(os.path.join(os.path.abspath(mask_directory), file_type)))

# loop all mask files
for file in list_of_mask_files:
    mask_img = PillImage(file)
    bbox = mask_img.get_bbox()
    basename = os.path.basename(file)
    for dir in image_root_dirs:
        crop_dir_images(dir, bbox)
            

        
        
    