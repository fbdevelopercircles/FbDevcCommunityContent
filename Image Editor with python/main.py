'''
To create a program that converts jpg images to png images
It loops through a picture folder,
converts the pictures with .jpg format into the .png format,
and saves them in a new folder.
-Create a parent folder XYZ
-Create a folder that would hold your pictures (in the .jpg format)
-Your python script should be saved in the parent folder XYZ
- while running the program from the command line, remember to include a '/' after specifying the folders,
you want to work with.
- feel free to edit the pictures, all editing effects would take place at once
-feel free to input print statements to check if your code is running correctly
'''

import sys
import os
from PIL import Image,ImageFilter
#get the first two indexes which are (image folder and the new folder to hold our converted pictures)
pictures_folder = sys.argv[1]
output_folder = sys.argv[2]
size = (128,128) #a thumbnail sized image

#check if the new folder exists, if not, create it
if not os.path.exists('edited-images'):
    os.makedirs('edited-images')

#loop through picture folder and convert pictures to .png and save to the new folder
for filename in os.listdir(pictures_folder):
    #print(filename)
    new_picture = Image.open(f'{pictures_folder}{filename}')
    final_name = os.path.splitext(filename)[0]
    new_picture.filter(ImageFilter.SMOOTH) #smoothens all converted pictures
    new_picture.thumbnail(size) #converts all pictures to a thumbnail
    #print(final_name)
    new_picture.save(f'{output_folder}{filename}.png', 'png')
    print('All pictures converted')