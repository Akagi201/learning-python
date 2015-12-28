#!/usr/bin/env python

import imageio

im = imageio.imread('akhead.png')
print(im.shape) # im is a numpy array
imageio.imwrite('akhead-gray.jpg', im[:,:,0])
