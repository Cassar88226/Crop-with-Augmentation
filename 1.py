import random
import Augmentor
import math

from numpy.random.mtrand import rand

count = 10

for x in range(count):
    p1 = Augmentor.Pipeline("./1")
    rotation = random.randint(0,25)
    rotationisleftorright = random.randint(0,1)
    p1.rotate(probability=0.7, max_left_rotation=rotation, max_right_rotation=rotationisleftorright)

    flipleftrightpro = random.randint(0,1)
    p1.flip_left_right(flipleftrightpro)

    fliptopbottompro = random.randint(0,1)
    p1.flip_top_bottom(fliptopbottompro)

    zoomfactor = random.uniform(1,1.3)
    p1.zoom(probability=1, min_factor=zoomfactor, max_factor=1.5)

    shearamount = random.randint(-10,10)
    sheardir = random.randint(0,1)
    p1.shear(probability=1, max_shear_left=shearamount, max_shear_right=sheardir)
    
    # elastic deformation
    distomagnitude = random.uniform(-10, 10)
    p1.elastic_deformation(probability=1, grid_width=4, grid_height=4, magnitude=distomagnitude)

    # random translate
    x_shift_factor = random.uniform(-0.2,0.2)
    y_shift_factor = random.uniform(-0.2,0.2)
    p1.random_translate(probability=1, x_shift=x_shift_factor, y_shift=y_shift_factor)
    
    # random contrast
    contrast_factor = random.uniform(0.3,1.7)
    p1.random_contrast(probability=1, factor=contrast_factor)
    
    # random stretch
    x_factor = random.uniform(0.7, 1.3)
    y_factor = random.uniform(0.7, 1.3)
    p1.random_stretch(probability=1, x_factor=x_factor, y_factor=y_factor)
    
    p1.sample(count = x, multi_threaded = False)

    p2 = Augmentor.Pipeline("./2")
    p2.rotate(probability=0.7, max_left_rotation=rotation, max_right_rotation=rotationisleftorright)
    p2.flip_left_right(flipleftrightpro)
    p2.flip_top_bottom(fliptopbottompro)
    p2.zoom(probability=1, min_factor=zoomfactor, max_factor=1.5)
    p2.shear(probability=1, max_shear_left=shearamount, max_shear_right=sheardir)
    p2.elastic_deformation(probability=1, grid_width=4, grid_height=4, magnitude=distomagnitude)
    p2.random_translate(probability=1, x_shift=x_shift_factor, y_shift=y_shift_factor)
    p2.random_contrast(probability=1, factor=contrast_factor)
    p2.random_stretch(probability=1, x_factor=x_factor, y_factor=y_factor)
    p2.sample(count = x, multi_threaded=False)

    p3 = Augmentor.Pipeline("./3")
    p3.rotate(probability=0.7, max_left_rotation=rotation, max_right_rotation=rotationisleftorright)
    p3.flip_left_right(flipleftrightpro)
    p3.flip_top_bottom(fliptopbottompro)
    p3.zoom(probability=1, min_factor=zoomfactor, max_factor=1.5)
    p3.shear(probability=1, max_shear_left=shearamount, max_shear_right=sheardir)
    p3.elastic_deformation(probability=1, grid_width=4, grid_height=4, magnitude=distomagnitude)
    p3.random_translate(probability=1, x_shift=x_shift_factor, y_shift=y_shift_factor)
    p3.random_contrast(probability=1, factor=contrast_factor)
    p3.random_stretch(probability=1, x_factor=x_factor, y_factor=y_factor)
    p3.sample(count = x, multi_threaded=False)

    p4 = Augmentor.Pipeline("./4")
    p4.rotate(probability=0.7, max_left_rotation=rotation, max_right_rotation=rotationisleftorright)
    p4.flip_left_right(flipleftrightpro)
    p4.flip_top_bottom(fliptopbottompro)
    p4.zoom(probability=1, min_factor=zoomfactor, max_factor=1.5)
    p4.shear(probability=1, max_shear_left=shearamount, max_shear_right=sheardir)
    p4.elastic_deformation(probability=1, grid_width=4, grid_height=4, magnitude=distomagnitude)
    p4.random_translate(probability=1, x_shift=x_shift_factor, y_shift=y_shift_factor)
    p4.random_contrast(probability=1, factor=contrast_factor)
    p4.random_stretch(probability=1, x_factor=x_factor, y_factor=y_factor)
    p4.sample(count=x, multi_threaded=False)