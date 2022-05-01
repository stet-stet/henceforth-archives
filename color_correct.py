import os
from PIL import Image
import numpy as np
import colorsys
import shutil

SOURCE_DIR = '!assembly'
TARGET_DIR = '!assembly_cc'

rgb_to_hsv = np.vectorize(colorsys.rgb_to_hsv)
hsv_to_rgb = np.vectorize(colorsys.hsv_to_rgb)

from_arr = [x/360 for x in [0,118,134,344,360]]
to_arr = [x/360 for x in [36,60,190,246,396]]

def shift_hue(arr):
    r, g, b, a = np.rollaxis(arr, axis=-1)
    h, s, v = rgb_to_hsv(r, g, b)
    h = np.interp(h, from_arr, to_arr)
    r, g, b = hsv_to_rgb(h, s, v)
    arr = np.dstack((r, g, b, a))
    return arr

def colorize(image):
    img = image.convert('RGBA')
    arr = np.array(np.asarray(img).astype('float'))
    new_img = Image.fromarray(shift_hue(arr).astype('uint8'), 'RGBA')

    return new_img

def convert(file, outfile):
    im = Image.open(file)
    im2 = colorize(im)
    im2.save(outfile)

def predicate(integer):
    if integer >= 359 and integer <= 379:
        return False 
    elif integer>=1959 and integer <= 1979: 
        return False
    elif integer>=2630 and integer<=2650:
        return False 
    return True


if __name__ == '__main__':
    files = os.listdir(SOURCE_DIR)
    for file in files:
        print('Processing %s' % file)
        in_file = r'%s/%s' % (SOURCE_DIR, file)
        out_file = r'%s/%s' % (TARGET_DIR, file)
        if predicate(int(file.split('.')[0])):
            convert(in_file, out_file)
        else:
            shutil.copy(in_file,out_file)