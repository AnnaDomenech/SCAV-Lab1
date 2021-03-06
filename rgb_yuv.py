#rgb to yuv
def _yuv(r, g, b): # in (0,255) range
    y = .257*r + .504*g + .098*b + 16
    cb = 128.0 -.148*r -.291*g + .439*b
    cr = 128.0 +.439*r - .368*g - .071*b
    return y, cb, cr
#yuv to rgb
def _rgb(y, cb, cr):
    r = 1.164*(y-16.0) + 1.596 * (cr-128)
    g = 1.164*(y-16.0)- .813 * (cr-128) -  .391 * (cb-128)
    b = 1.164*(y-16.0) + 2.018 * (cb-128)
    return r, g, b

    
if __name__ == "__main__": 
    print('[a] RGB to YcrCb\n[b] YcrCb to RGB\n[c] Exit')
    x = str(input())
    while not x =='c':
        if x=='a':
            inp = list(map(int, input("Enter the RGB color you want to convert: ").split()))
            print("RGB: ", inp)
            outp = _yuv(inp[0],inp[1],inp[2])
            print("YCrCb: ", outp)
        elif x=='b':
            inp = list(map(int, input("Enter the YCrCb color you want to convert: ").split()))
            print("YCrCb: ", inp)
            outp = _rgb(inp[0],inp[1],inp[2])
            print("RGB: ", outp)
        else:
            print("error")
            pass
        print('[a] RGB to YcrCb\n[b] YcrCb to RGB\n[c] Exit')
        x = str(input())