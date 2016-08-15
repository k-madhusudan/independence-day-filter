from skimage import data
import skimage
import os
from skimage import io
import matplotlib.pyplot as plt
from skimage.color import rgb2gray

cam = data.camera()
print type(cam)
print cam.shape
filename = os.path.join("/home/madhusudan/Programming/Python-For-Life/independence-day-filter","lena.png")
lena = io.imread(filename)
print type(lena)
print lena.shape

rgblena = rgb2gray(lena)



#io.imshow(lena,plugin=None)
io.imshow(rgblena, plugin=None)
io.show()
print lena.min(), lena.max()
#plt.imshow(lena)
#plt.show()