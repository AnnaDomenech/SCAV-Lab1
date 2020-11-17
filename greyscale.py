from pathlib import Path
import os
class iodir:
    inp : str
    outp : str
    def __init__(self,inp,outp):
        self.inp=inp
        self.outp=outp

def setDir():
    name = "Lenna.jpg"
    input_path= Path.cwd()
    file_path= [ subp for subp in input_path.iterdir() if subp.match(name)]
    file_path.sort()
    output_path =  Path.cwd() / "Results"
    output_path.mkdir(parents=True, exist_ok=True)
    return iodir(str(file_path[0].name),output_path)

if __name__ == "__main__": 
    dyr=setDir()
    output = str(dyr.outp / "Lenna_greyscale.jpg")
    command = f"ffmpeg -i {dyr.inp}  -pix_fmt yuvj422p -vf hue=s=0 {output}"
    os.system(command)

