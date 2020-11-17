def _ycc(r, g, b): # in (0,255) range
    y = round(.299*r + .587*g + .114*b)
    cb = round(128 -.168736*r -.331364*g + .5*b)
    cr = round(128 +.5*r - .418688*g - .081312*b)
    return y, cb, cr

def _rgb(y, cb, cr):
    r = int(y + 1.402 * (cr-128))
    g = int(y - .34414 * (cb-128) -  .71414 * (cr-128))
    b = int(y + 1.772 * (cb-128))
    return r, g, b

    
if __name__ == "__main__": 
    print('[a] RGB to YcrCb'); print('[b] YcrCb to RGB');print('[c] Exit')
    x = str(input())
    while not x =='c':
        if x=='a':
            inp = list(map(int, input("Enter the RGB color you want to convert: ").split()))
            print("RGB: ", inp)
            outp = _ycc(inp[0],inp[1],inp[2])
            print("YCrCb: ", outp)
        elif x=='b':
            inp = list(map(int, input("Enter the YCrCb color you want to convert: ").split()))
            print("YCrCb: ", inp)
            outp = _rgb(inp[0],inp[1],inp[2])
            print("RGB: ", outp)
        else:
            print("error")
            pass
        print('[a] RGB to YcrCb'); print('[b] YcrCb to RGB');print('[c] Exit')
        x = str(input())