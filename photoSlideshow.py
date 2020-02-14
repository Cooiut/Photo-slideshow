#  Copyright (c) 2020.
#  This problem is from Online Qualication Round of Hash Code 2019
#  Contributor: Cooiut, Jason, Jiahao Chen

numOfPhoto = 0
photo = dict()
image_orientation = dict()
output = []

def photo_slideshow(infile, outfile):
    fin = open(infile, 'r')
    numOfPhoto = fin.readline()
