# bird_detect
Detect bird species in photos using YOLOv3

# Downloading, augmenting and labelling data

- First download OpenLabelling
```bash
git clone https://github.com/Cartucho/OpenLabeling
```
- Move the files from /label/ into the OpenLabeling repo /OpenLabeling/main
- Now get the csv of birds you want to scrape and download from the macaulay library.
- I already have some in the repository. 
- You have to make an account to download big csv.
- Edit the download_birds.py to include these csv.
- Now to download those bird images run 
```bash
make all
```
- This downloads the files, splits them into train,test,val folders, and runs augmentation 
to increase the size of the dataset. 
- Now we move them to the OpenLabelling directory
```
make move
```
- Now change to the openlabelling directory and label some training images with
```
make tr
```
- Label testing images with
```
make te
```
- Label validation images with
```
make v
```

# Training model 
- Download the ipynb file bird_YOLO_v3.ipynb
- Upload this file to colab to run
- Compress your train,test,val folders (including "out" label folders) in a folder called 'bird_data'. Upload it to your google drive
- Note: the train folder will need to be compressed otherwise it will be too large.
- Put the train and train_out folders into a zip folder named 'trains' inside 'bird_data'
- Run all in the ipynb. It should take 2+ hours to train(with premium) more with free colab
- Note: colab will need permission to grab the data from your drive
- You can see the saved results on video and image tests in your drive
