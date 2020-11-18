# SCAV - Lab 1
For this lab we will use the Lenna image for the exercices require an input image:

![Lenna resize](/Lenna.jpg)

## RGB to YUV and YUV to RGB
Execute the rgb_yuv.py file and enter a RGB/YUV value in the terminal and obtain its YUV/RGB value.
## Scaling exercice
To resize the image we can take into account different compression ratios. In order to implement that, we have used the command:"ffmpeg -i input -vf scale=iw*.{x}:ih*.{x} output" where x is the compression ratio entered by the user in the terminal.

![Lenna resize 25](/Results/Lenna_resize0.jpg)
![Lenna resize 50](/Results/Lenna_resize1.jpg)
![Lenna resize 70](/Results/Lenna_resize2.jpg)
![Lenna resize 90](/Results/Lenna_resize3.jpg)

Here we have the results of different compression ratio corresponding to 25%, 50%, 70% and 90%.
## Greyscale exercice
To convert Lenna to the greyscale image we have used the following command: "ffmpeg -i input  -pix_fmt yuvj422p -vf format=gray output".
The -pix_fmt yuvj422p is used to change the pixel format by applying the chroma subsampling and using a 4:2:0,i.e, Cb' and Cr' are each subsampled at a factor of two, both horizontally and verticall. Since we want that a greyscale result image we do not need to have a good quality in the chroma planes. The unique plane that interest us is the luminance, to give this importance to the luminance plane we use -vf format=gray or -vf h=s=0. Both works, and with both we achieve that the resulting image have a size of 10KB.

![Lenna gray](/Results/Lenna_greyscale.jpg)

## Run-lenght encoder
Execute the run_lenght_encoder.py file and enter a byte sequence to obtain its codification.

## DCT encoder and decoder
This script encodes and decodes a jpg image by using the dct. By using the dct and idct on Lenna.jpg image we obtain a image of []KB. 
Also we can use a threshold to define the number of DCT coefficients that we want to keep, the threshold can have a value between 0 and 1. If we set it to 0, we will use all the dct coefficients, and if we set it to 1 we won't keep non(no sense). This threshold is used in the following sense: it take the maximum value of de dct and then multiplies it by the threshold, then all the dct values that are bigger than the max(dct)·thr will be keeped. Notice that the thr effect will change depending on the input image.

![Lenna resize 25](/Results/Lenna_dct0.jpg)
![Lenna resize 50](/Results/Lenna_dct1.jpg)
![Lenna resize 70](/Results/Lenna_dct2.jpg)
