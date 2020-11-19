import os
from pathlib import Path
import numpy as np
import scipy.fftpack as fftpack
import imageio
from numpy import zeros
from numpy import r_
class iodir:
    inp : str
    outp : str
    def __init__(self,inp,outp):
        self.inp=inp
        self.outp=outp
#2D dct
def dct2(a):
    return fftpack.dct( fftpack.dct( a, axis=0, norm='ortho' ), axis=1, norm='ortho' )
#2D idct
def idct2(a):
    return fftpack.idct( fftpack.idct( a, axis=0 , norm='ortho'), axis=1 , norm='ortho')

def setDir():
    name = "Lenna.jpg"
    input_path= Path.cwd()#get current directory
    #for each file in folder get input path (Lenna.jpg)
    file_path= [ subp for subp in input_path.iterdir() if subp.match(name)]
    file_path.sort()
    output_path =  Path.cwd() / "Results"#set output folder path 
    output_path.mkdir(parents=True, exist_ok=True)# create it 
    return iodir(str(file_path[0].name),output_path)


def dct(dct_thresh,imsize):
    dct = np.zeros(imsize)
    # Do 8x8 DCT on image 
    for i in r_[:imsize[0]:8]:
        for j in r_[:imsize[1]:8]:
            #for 8x8 block we apply dct
            dct[i:(i+8),j:(j+8)] = dct2( im[i:(i+8),j:(j+8)] )
    return  dct 

def idct(dct_thresh,imsize):
    im_dct = np.zeros(imsize)
    for i in r_[:imsize[0]:8]:
        for j in r_[:imsize[1]:8]:
            #for 8x8 block we apply idct
            im_dct[i:(i+8),j:(j+8)] = idct2( dct_thresh[i:(i+8),j:(j+8)] )
    return im_dct 

if __name__ == "__main__": 
    dyr=setDir()
    im = imageio.imread(dyr.inp).astype(float)
    imsize = im.shape
    count=0
    dct = dct(im, imsize)
    thresh = input("Enter a threshold between 0 and 1 .\n 0 to avoid thresholding \n Example: 0.005-0.012-0.1\n")
    while not thresh ==  '-1':
        dct_thresh = dct * (abs(dct) > (float(thresh)*np.max(dct)))#keep dct coefficients bigger than thresh*np.max(dct)
        im_dct = idct(dct_thresh,imsize)
        output = str(dyr.outp / "Lenna_dct{:}.jpg".format(count))#set output file name
        imageio.imwrite(output, np.uint8(im_dct))#save image
        count+=1
        thresh = input("Enter a threshold between 0 and 1 to decide the number of dct coefficients we will keep. \n Enter -1 to exit\n")
