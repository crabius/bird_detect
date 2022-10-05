"""
Perform data augmentation on images files in
FROM, the input folder and output the images in 
TO, the output folder.
Doubles amount of data by appling a couple of transformations
"""

from PIL import Image
import numpy as np
import albumentations as A
import matplotlib.pyplot as plt
import os

#folders we are reading from and writing to
FROM='./images'
TO='./target'

# Declare an augmentation pipeline
transform = A.Compose([
    A.HorizontalFlip(p=1.0),
    A.GridDropout(unit_size_min=0,
                  unit_size_max=1,
                  holes_number_x=70,
                  holes_number_y=70,
                  p=1.0
                  ),
    A.ColorJitter(p=1.0)
])

#enumerate over images
for i,img in enumerate(os.listdir(FROM)):
    name = f'{FROM}/{img}'
    image = Image.open(name)
    image = np.asarray(image)
    #transform image
    transformed = transform(image=image)
    image = transformed["image"]
    image = Image.fromarray(image)
    image.save(f'{TO}/{i}.png')
