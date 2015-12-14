from tkinter.filedialog import askopenfilename
from PIL import Image
import random
import sys
from bisect import bisect
file = askopenfilename()
picture=Image.open(file)
picture=picture.resize((75, 75), Image.ANTIALIAS)
picture=picture.convert("L") # Mono conversion for picture
# 7 different colors of greyscale/black and white picture
# pictures a different character for each tone of darkness
# only if possible. 
 
greyscale = [
            " ",
            " ",
            ".,-",
            "_ivc=!/|\\~",
            "gjez2]/(YL)t[+T7Vf",
            "mdK4ZGbNDXY5P*Q",
            "W8KMA",
            "#%$"
            ]
 
#bisecs values and creates ranges 
 
ranges=[36,72,108,144,180,216,252]
#
 
# open image and resize
# experent with aspect ratios according to font
 
picture=Image.open(file)
picture=picture.resize((160, 75),Image.BILINEAR)
picture=picture.convert("L") # convert to mono
 
# now, work our way over the pixels
# build up str
 
str=""
for y in range(0,picture.size[1]):
    for x in range(0,picture.size[0]):
        pixel=255-picture.getpixel((x,y))
        row=bisect(ranges,pixel)
        possibleChar=greyscale[row]
        str=str+possibleChar[random.randint(0,len(possibleChar)-1)]
    str=str+"\n"
 
print (str)
