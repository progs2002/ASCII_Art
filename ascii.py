import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('input2.jpg')

g_img2 = 0.2126 * img[:,:,0] + 0.7152 * img[:,:,1] + 0.0722 * img[:,:,2]


if g_img2.shape[0] % 2 != 0:
    g_img2 = g_img2[:-1,:]


ascii_map = "@%#*+=-:. "

l = len(ascii_map)
m = l/256 

str = ""

for i in range(0,g_img2.shape[0],2):
    for j in range(g_img2.shape[1]):
        v = (g_img2[i,j] + g_img2[i+1,j])/2
        str += ascii_map[int(m*v)]
    str += "\n"

print(str)

file_out = open("output.txt",'w')
file_out.write(str)