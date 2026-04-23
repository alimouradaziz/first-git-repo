# Code sourced from https://subscription.packtpub.com/book/data/9781800201774/2/ch02lvl1sec10/image-arithmetic
# Image source: https://www.gnu.org/graphics/wallpapers.en.html

# Import libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt
#matplotlib inline

# Read image
img = cv2.imread("einstein.png")
print(img.shape)

# Display image
plt.imshow(img[:,:,::-1])
plt.show()

# Add 100 to the image
numpyImg = img+100
# Notice how adding the value 100 has distorted the image severely.
# This is because of the modulo operation being performed by NumPy
# on the new pixel values. This should also give you an idea of
# why NumPy's approach is not the recommended approach to use
# while dealing with adding a constant value to an image.

# Display image
plt.imshow(numpyImg[:,:,::-1])
plt.show()

# Using OpenCV
opencvImg = cv2.add(img,100)

# Display image
plt.imshow(opencvImg[:,:,::-1])
plt.show()
# As shown in the preceding figure,
# there is an increased blue tone to the image.
# This is because the value 100 has only been added
# to the first channel of the image, which is the blue channel.


nparr = np.ones(img.shape,dtype=np.uint8) * 100

opencvImg = cv2.add(img,nparr)
# Display image
plt.imshow(opencvImg[:,:,::-1])
plt.show()



