import os, sys
from PIL import Image


image_1 = Image.open("sample1.jpg")     #Load the original size of sample jpeg image (4.5MB)
image_2 = Image.open("sample2.jpg")     #Load a smaller size of jpeg image (100KB)

image_1.show()
image_2.show()

print(image_1.format, image_1.size, image_1.mode)
print(image_2.format, image_2.size, image_2.mode)

