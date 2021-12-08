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


    distomagnitude = random.uniform(-4, 4)
    p1.random_distortion(probability=1, grid_width=4, grid_height=4, magnitude=distomagnitude)

    shearamount = random.randint(-10,10)
    sheardir = random.randint(0,1)
    p1.shear(probability=1, max_shear_left=shearamount, max_shear_right=sheardir)
    p1.sample(count = x, multi_threaded = False)

    p2 = Augmentor.Pipeline("./2")
    p2.rotate(probability=0.7, max_left_rotation=rotation, max_right_rotation=rotationisleftorright)
    p2.flip_left_right(flipleftrightpro)
    p2.flip_top_bottom(fliptopbottompro)
    p2.zoom(probability=1, min_factor=zoomfactor, max_factor=1.5)
    p2.random_distortion(probability=1, grid_width=4, grid_height=4, magnitude=distomagnitude)
    p2.shear(probability=1, max_shear_left=shearamount, max_shear_right=sheardir)
    p2.sample(count = x, multi_threaded=False)

    p3 = Augmentor.Pipeline("./3")
    p3.rotate(probability=0.7, max_left_rotation=rotation, max_right_rotation=rotationisleftorright)
    p3.flip_left_right(flipleftrightpro)
    p3.flip_top_bottom(fliptopbottompro)
    p3.zoom(probability=1, min_factor=zoomfactor, max_factor=1.5)
    p3.random_distortion(probability=1, grid_width=4, grid_height=4, magnitude=distomagnitude)
    p3.shear(probability=1, max_shear_left=shearamount, max_shear_right=sheardir)
    p3.sample(count = x, multi_threaded=False)

    p4 = Augmentor.Pipeline("./4")
    p4.rotate(probability=0.7, max_left_rotation=rotation, max_right_rotation=rotationisleftorright)
    p4.flip_left_right(flipleftrightpro)
    p4.flip_top_bottom(fliptopbottompro)
    p4.zoom(probability=1, min_factor=zoomfactor, max_factor=1.5)
    p4.random_distortion(probability=1, grid_width=4, grid_height=4, magnitude=distomagnitude)
    p4.shear(probability=1, max_shear_left=shearamount, max_shear_right=sheardir)
    p4.sample(count=x, multi_threaded=False)