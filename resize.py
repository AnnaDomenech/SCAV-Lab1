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
    dyr=setDir()#set directories
    count=0
    aux = input("Enter compress ratio without %:")
    while not aux == 'c':
        if aux == '0':
            print("with this compress ratio you will not apply resizing")
        else:
            x = 100 - int(aux)#Compression ratio of 25% == 0.75 * original size
            output = str(dyr.outp / "Lenna_resize{:}.jpg".format(count))#set output image name
            command = f"ffmpeg -i {dyr.inp} -vf scale=iw*.{x}:ih*.{x} {output}"#ffmpeg command
            os.system(command)
            
        aux = input("Enter compress ratio without %\nPress c to exit:")
        count+=1
