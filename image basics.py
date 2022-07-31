# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 23:53:10 2022

@author: Brent
"""

import PIL
img = PIL.Image.open("rose.jpg")
img.show()
print(img.format, img.size, img.mode)
