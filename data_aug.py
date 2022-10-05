from PIL import Image
import numpy as np
import albumentations as A
import os

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

def data_aug(name,FROM,TO):
    """
    Perform data augmentation on images files in
    FROM, the input folder and output the images in 
    TO, the output folder.
    in format name_i.png where i is an int
    """
    
    #items already in augmented dir
    target_dir = os.listdir(TO)
    
    #enumerate over images
    for i,img in enumerate(os.listdir(FROM)):
        name = f'{FROM}/{img}'
        image = Image.open(name)
        image = np.asarray(image)
        #transform image
        transformed = transform(image=image)
        image = transformed["image"]
        image = Image.fromarray(image)
        if f'{i}.png' not in target_dir:
        	#avoid saving duplicates
        	image.save(f'{TO}/{bird}_{i}.png')

if __name__=="__main__":
    #lets run data augmentation on all our birds
    for bird in ['kea','takahe','tui']:
        data_aug(bird,f'./input/{bird}',f'./train')
