from pathlib import Path
import os

#iodir: input and output directory class
class iodir:
    inp : str
    outp : str
    def __init__(self,inp,outp):
        self.inp=inp
        self.outp=outp

def setDir():
    name = "Lenna.jpg"
    input_path= Path.cwd()#get current directory
    #for each file in folder get input path (Lenna.jpg)
    file_path= [ subp for subp in input_path.iterdir() if subp.match(name)]
    file_path.sort()
    output_path =  Path.cwd() / "Results"#set output folder path 
    output_path.mkdir(parents=True, exist_ok=True)# create it 
    return iodir(str(file_path[0].name),output_path)

if __name__ == "__main__": 
    dyr=setDir()
    output = str(dyr.outp / "Lenna_greyscale.jpg")#set output image name
    #ffmpeg command
    # -pix_fmt yuvj420 to apply 4:2:0 chroma subsample
    # -vf hue=s=0 to desaturate or -vf format=gray to grayscale.
    command = f"ffmpeg -i {dyr.inp}  -pix_fmt yuvj420p -vf format=gray   {output}"
    os.system(command)

