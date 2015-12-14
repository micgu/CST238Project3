#Team Sakanoto or whatever. Teammates were Michael Gu and Miguel Lopez

import os, sys
from PIL import Image
import numpy
import matplotlib.pyplot as plt
import glob
import image_slicer
from PIL import ImageDraw, ImageFont
import math

def meanPixel(tile):
    rt = 0
    gt = 0
    bt = 0
    for pixel in tile:
        r, g, b = pixel
        rt = rt + r
        gt = gt + g
        bt = bt + b
    mean = [math.floor(rt / len(tile)), math.floor(gt / len(tile)), math.floor(bt / len(tile))]
    return mean
folder = "/Users/localadmin/Documents/205/images/Image"
pictures = []
pic = Image.open(folder + "1.jpg")
pictures.append(pic)
pic = Image.open(folder + "2.jpg")
pictures.append(pic)
pic = Image.open(folder + "3.jpg")
pictures.append(pic)
pic = Image.open(folder + "4.jpg")
pictures.append(pic)
pic = Image.open(folder + "5.jpg")
pictures.append(pic)

puzzle = Image.new('RGB', pictures[0].size, color=0)

width, height = puzzle.size
p = puzzle.load()
pixelSize = 5
hr = int(math.ceil(height / int(pixelSize)))
wr = int(math.ceil(width / int(pixelSize)))
tiles = [[[]for i in range(int(hr))]for j in range(int(wr))]
for x in range(width):
    for y in range(height):
        tiles[int(math.floor(x / pixelSize) - 1)][int(math.floor(y / pixelSize) - 1)].append(pictures[0].getpixel((x, y)))

meanArray = [([0] * hr)for k in range(wr)]
for metaX in range(wr):
    for metaY in range(hr):
        meanArray[metaX][metaY] = meanPixel(tiles[metaX][metaY])
pixelData = puzzle.load()
for x in range(width):
    for y in range(height):
        r = int(meanArray[int(math.floor(x / pixelSize)) -1 ][int(math.floor(y / pixelSize)) -1][0])
        print int(math.floor(x / pixelSize)) - 1
        print int(math.floor(y / pixelSize)) -1
        g = int(meanArray[int(math.floor(x / pixelSize))-1][int(math.floor(y / pixelSize))-1][1])
        b = int(meanArray[int(math.floor(x / pixelSize))-1][int(math.floor(y / pixelSize))-1][2])
        pixelData[x, y] = (r, g, b)







puzzle.show()