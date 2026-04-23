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

# Multiply the image by 2 using the cv2.multiply function:
cvImg = cv2.multiply(img,2)

# Display image
plt.imshow(cvImg[:,:,::-1])
plt.show()

# Try to multiply the image using NumPy:
npImg = img*2

# Display image
plt.imshow(npImg[:,:,::-1])
plt.show()


nparr = np.ones(img.shape,dtype=np.uint8) * 2

cvImg = cv2.multiply(img,nparr)
plt.imshow(cvImg[:,:,::-1])
plt.show()





