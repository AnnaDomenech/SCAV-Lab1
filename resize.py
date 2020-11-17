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
    count=0
    print("Enter compress ratio without %:")
    aux = input()
    while not aux =='c':
        x = 100- int(aux)
        output = str(dyr.outp / "Lenna_resize{:}.jpg".format(count))
        command = f"ffmpeg -i {dyr.inp} -vf scale=iw*.{x}:ih*.{x} {output}"
        os.system(command)
        print("Enter compress ratio without %:")
        print("Press c to exit")
        aux = str(input())
        count+=1
