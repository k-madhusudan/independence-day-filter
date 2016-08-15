from skimage import data
import skimage
import os
from skimage import io
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage import img_as_float
from skimage import color
# Saffron : 255, 153, 51
#cam = data.camera()
#print type(cam)
#print cam.shape
filename = os.path.join("/home/madhusudan/Programming/Python-For-Life/independence-day-filter","lena.png")
lena = io.imread(filename)
#print type(lena)
#print lena.shape

rgblena = rgb2gray(lena)
print type(rgblena)
print rgblena.shape

lenaimg = img_as_float(rgblena)

saffron_mult = [1,153.0/255.0,51/255.0]
white_mult = [1,1,1]
green_mult = [19.0/255,136.0/255,8.0/255]

lenacolor= color.gray2rgb(lenaimg)
#io.imshow(lena,plugin=None)

lenacolor[0: lenacolor.shape[0]/3] = lenacolor[0: lenacolor.shape[0]/3] * saffron_mult
lenacolor[(lenacolor.shape[0]/3)*1: (lenacolor.shape[0]/3)*2] = lenacolor[(lenacolor.shape[0]/3)*1: (lenacolor.shape[0]/3)*2] * white_mult
lenacolor[(lenacolor.shape[0]/3)*2: (lenacolor.shape[0]/3)*3] = lenacolor[(lenacolor.shape[0]/3)*2: (lenacolor.shape[0]/3)*3] * green_mult

io.imshow(lenacolor, plugin=None)
io.show()
print rgblena.min(), rgblena.max()
#plt.imshow(lena)
#plt.show()