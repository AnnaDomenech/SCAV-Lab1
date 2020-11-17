import os
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import scipy
import imageio

from numpy import pi
from numpy import sin
from numpy import zeros
from numpy import r_
from scipy import signal
from scipy import misc # pip install Pillow
import matplotlib.pylab as pylab
pylab.rcParams['figure.figsize'] = (20.0, 7.0)
class iodir:
    inp : str
    outp : str
    def __init__(self,inp,outp):
        self.inp=inp
        self.outp=outp

def dct2(a):
    return scipy.fftpack.dct( scipy.fftpack.dct( a, axis=0, norm='ortho' ), axis=1, norm='ortho' )

def idct2(a):
    return scipy.fftpack.idct( scipy.fftpack.idct( a, axis=0 , norm='ortho'), axis=1 , norm='ortho')

def setDir():
    name = "Lenna.jpg"
    input_path= Path.cwd()
    file_path= [ subp for subp in input_path.iterdir() if subp.match(name)]
    file_path.sort()
    output_path =  Path.cwd() / "Results"
    output_path.mkdir(parents=True, exist_ok=True)
    return iodir(str(file_path[0].name),output_path)

def idct(dct_thresh,imsize):
    im_dct = np.zeros(imsize)
    for i in r_[:imsize[0]:8]:
        for j in r_[:imsize[1]:8]:
            im_dct[i:(i+8),j:(j+8)] = idct2( dct_thresh[i:(i+8),j:(j+8)] )
    return im_dct 

def dct(dct_thresh,imsize):
    dct = np.zeros(imsize)
    # Do 8x8 DCT on image (in-place)
    for i in r_[:imsize[0]:8]:
        for j in r_[:imsize[1]:8]:
            dct[i:(i+8),j:(j+8)] = dct2( im[i:(i+8),j:(j+8)] )
    return  dct 


if __name__ == "__main__": 
    dyr=setDir()
    im = imageio.imread(dyr.inp).astype(float)
    imsize = im.shape
    count=0
    dct = dct(im, imsize)
    print("Enter a threshold between 0 and 1 .\n 0 to avoid thresholding \n Example: 0.005-0.012-0.1")
    thresh = input()
    while not thresh ==  '-1':
        dct_thresh = dct * (abs(dct) > (float(thresh)*np.max(dct)))
        percent_nonzeros = np.sum( dct_thresh != 0.0 ) / (imsize[0]*imsize[1]*1.0)
        print("Keeping {:.2f}% of the {:} DCT coefficients".format(percent_nonzeros*100.0, len(dct)))
        im_dct = idct(dct_thresh,imsize)
        output = str(dyr.outp / "Lenna_dct{:}.jpg".format(count))
        imageio.imwrite(output, np.uint8(im_dct))
        count+=1
        print("Enter a threshold between 0 and 1 to decide the number of dct coefficients we will keep. \n Enter -1 to exit")
        thresh = input()
