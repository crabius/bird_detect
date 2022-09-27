#!/usr/bin/env python3
"""
Taken from 
https://github.com/ankurdave/macaulay-bird-species-pittsburgh/blob/master/scrape-macaulay-search-csv.py
"""
"""
Allows scraping thumbnails from the Macaulay Library based on a CSV from a search.
For example, here is a search for images of Mourning Dove:
https://search.macaulaylibrary.org/catalog?mediaType=photo&unconfirmed=incl&captive=incl&taxonCode=moudov&view=list
"""
import splitfolders
import csv
import requests
import sys
import os
import os.path
from PIL import Image

csv_to_dir = [
    ('10k_kea.csv', 'input/kea'),
]

def get_image(ml_catalog_number, output_dir):
    img = f"{output_dir}/{ml_catalog_number}.jpg"
    if os.path.exists(img):
        print(f"{img}: exists")
        return
    url = f"https://cdn.download.ams.birds.cornell.edu/api/v1/asset/{ml_catalog_number}/1200"
    print(f"{img} <- {url}")
    r = requests.get(url, allow_redirects=True)
    open(img, 'wb').write(r.content)


def load_ml_catalog_numbers(search_csv):
    # Keep one image per recordist to avoid duplicates.
    by_recordist = {}
    with open(search_csv, 'r') as f:
        reader = csv.reader(f)
        row_num = 0
        for row in reader:
            if row_num == 0:
                row_num += 1
                continue

            ml_catalog_number = row[0]
            recordist = row[5]
            rating = float(row[40]) if row[40] else 0.0

            if ((recordist in by_recordist and by_recordist[recordist][1] < rating)
                or (recordist not in by_recordist)):
                by_recordist[recordist] = (ml_catalog_number, rating)

            row_num += 1

    sorted_by_rating_desc = sorted(by_recordist.values(), key=lambda pair: pair[1], reverse=True)
    return [ml_catalog_number for (ml_catalog_number, rating) in sorted_by_rating_desc if rating > 0.0]

# RESIZE IMAGES
# https://stackoverflow.com/questions/21517879/python-pil-resize-all-images-in-a-folder
def resize(path,dirs,SZ):
    for item in dirs:
        print(item)
        print(path+item)
        if os.path.isfile(path+item):
            print("resizing")
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((SZ,SZ), Image.ANTIALIAS)
            imResize.save(f+".jpg", 'JPEG', quality=99)

if __name__ == "__main__":
    for (search_csv, output_dir) in csv_to_dir:
        ml_catalog_numbers = load_ml_catalog_numbers(search_csv)
        os.makedirs(output_dir, exist_ok=True)
        # Take the first 500 images.
        for cat_num in ml_catalog_numbers[0:10]:
            get_image(cat_num, output_dir)
        #resize images
        print(output_dir)
        print(os.listdir(output_dir))
        resize(output_dir+"/", os.listdir(output_dir), 400)
        # split into train, val, test folders
        splitfolders.ratio(
            "./input",
            output="output",
            seed=1337,
            ratio=(0.8,0.1,0.1)
        )
