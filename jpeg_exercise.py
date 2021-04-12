import os, sys
from PIL import Image

image_1 = Image.open("sample1.jpg")     #Load the original size of sample jpeg image (4.5MB)
image_2 = Image.open("sample2.jpg")     #Load a smaller size of jpeg image (100KB)

image_1.show()
image_2.show()

print(image_1.format, image_1.size, image_1.mode)
print(image_2.format, image_2.size, image_2.mode)

# You should write the code to do everything starting with sample1.jpg.  So, create cropped image like sample2.jpg from sample1.jpg programtically, in this python script.
# Exercises:
# Crop a 512px x 512px image from image_1
# Convert it to a numpy array
# Extract each of the three RGB channels as separate images
# Save these to file (and use .show() to display them on screen)
# Create a new image arranging the three channels side by side

# You could use these three small RGB images as a practice dataset to try out image alignment:
# https://learnopencv.com/feature-based-image-alignment-using-opencv-c-python/
