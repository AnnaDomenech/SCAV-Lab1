from collections import OrderedDict 

def runLengthEncoding(input): 
  
    # Generate ordered dictionary 
    dict=OrderedDict.fromkeys(input, 0) 
  
    # Iterate through input to calculate  
    # frequency of each character
    for ch in input: 
        dict[ch] += 1
  
    # now iterate through dictionary to make  
    # output as a set of (key,value) pairs 
    output = '' 
    for key,value in dict.items(): 
         output = output + key + str(value) 
    return output 
   
if __name__ == "__main__": 
    x = str(input("Enter the sequence of bits to encode:"))#get sequence
    while not x =='c':
        print ('The resulting encoded sequence is: ' + runLengthEncoding(x)) #apply run_length_encoding
        x = str(input("Enter the sequence of bits to encode\n Press c to exit\n"))
