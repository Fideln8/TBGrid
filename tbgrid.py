# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 18:34:00 2015

@author: nathanhoeft
"""

import os
from PIL import Image
scriptDir = os.path.dirname(__file__)

impath = os.path.join(scriptDir, '../Downloads/IMG_7835.JPG')

im = Image.open(impath)
im = im.rotate(90)

box = im.getbbox()

ppi = 300
width = box[2]
height = box[3]

grid = 100

crop_width = width/grid
crop_height = height/grid

grid_box = (0,0,crop_width, crop_height)
grid_count = grid
grid_images = []

image_count = 0

while grid_count > 0:
    row_count = grid
    while row_count > 0:
        image = im.crop(grid_box)
        grid_images.append(image)
        grid_box = list(grid_box)
        grid_box[0] += crop_width
        grid_box[2] += crop_width
        grid_box = tuple(grid_box)
        row_count -= 1
    grid_box = list(grid_box)
    grid_box[0] = 0
    grid_box[1] += crop_height 
    grid_box[2] = crop_width
    grid_box[3] += crop_height
    grid_box = tuple(grid_box)    
    image_count += 1
    grid_count -= 1
    
whitespace = grid * 5
test_size = (width+whitespace, height+whitespace)

test_image = Image.new("RGB", test_size, "white")
placement = (0,0)
placement_count = grid


while placement_count > 0:
    row_count = grid
    while row_count > 0:
        image = grid_images[0].rotate(10)
        test_image.paste(image,placement)
        placement = list(placement)
        placement[0] += crop_width + 5
        placement = tuple(placement)  
        grid_images.pop(0)
        row_count -= 1
    placement = list(placement)
    placement[0] = 0
    placement[1] += crop_height + 5
    placement = tuple(placement)
    placement_count -= 1

#test_image.save("test_image.jpeg")



    
    