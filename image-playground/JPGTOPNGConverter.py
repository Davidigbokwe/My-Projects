import sys
import os
from PIL import Image

#grab first and second arg
image_folder = sys.argv[1]
output_folder = sys.argv[2]

 
print(image_folder, output_folder)

#check if new exists else create it
if not os.path.exists(output_folder):
	os.makedirs(output_folder)

#loop through pokedex
for filename in os.listdir(image_folder):
	img = Image.open(f"{image_folder}{filename}")
	clean_name = os.path.splitext(filename)[0]
	img.thumbnail((266,266))

	#convert images to png

	img.save(f"{output_folder}{clean_name}.png", 'png')
	print("all done!")



# save to the new folder.

