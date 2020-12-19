def uncompress():
    """ extracts the contains of a compressed file
    """
    inputfile = askforinput()
    f = open(inputfile,"rb")
    readBytes = f.read()
    f.close()
    listOfBytes = list(readBytes)
    encodednums = numtobits(listOfBytes)
    restorednums = restore(encodednums,inputfile+".KEY") 
    keysdict = makedict(inputfile+".KEY")
    decodedtext= decode(restorednums, keysdict)
    f1 = open(inputfile+".DECODED", "w")
    f1.write(decodedtext)
    f1.close()



def askforinput():
    """ asks for user input of a file name
        makes sure the file name ends .HUFFMAN
    """
    while True:
        userinput = input("Enter a file to uncompress:")
        try:
            assert(userinput[-8:] == ".HUFFMAN")
        except (AssertionError):
            print("Please enter a file name that ends in .HUFFMAN")
            continue
        return userinput

def numtobits(listOfBytes):
    """ converts 8-bit nubmers into a string conatining an equivilant binary number
        input: listofbytes, list contianing 8-bit numbers
        output: a string containing the binary values of all numbers in the input list
    """
    output = ""
    for x in listOfBytes:
        output += EightBitNumToBinary(x)
    return output

def restore(nums, keysfile):
    """ restore removes the extra zeros added by EightBitsNumToBinary using the first line in the .KEY file
    """
    f = open(keysfile, "r")
    reallen = f.readline()
    numofchars = f.readline()
    numberofbits= f.readline()
    output = ""
    if len(nums) != int(reallen):
        diff = len(nums) - int(reallen)
        output = nums[:-8]+ nums[-(8-diff):]
    else:
        output = nums
    f.close()
    return output

def EightBitNumToBinary(num):
    """ converts an 8-bit number to a string conatining an equivilant binary number
    """
    output = ""
    while num > 0:
        if num % 2 == 0:
            output = "0" + output
        else:
            output = "1" + output
        num = int(num/2)
    padding = 8 - len(output)
    return padding * "0" + output

def makedict(keysfile):
    """ constructs a dict from a .KEY file
        input: keysfile, name of the file
        output: a dict with the prefixs (keys) refaring to their corresponding chars
    """
    f = open(keysfile, "r")
    reallen = f.readline()
    numofchars = f.readline()
    numberofbits= f.readline()
    output={}
    for x in range(int(numofchars)):
        char = f.read(1)
        key = f.readline()
        output[key[:-1]] = char
    f.close()
    return output

def decode(restorednums,keysdict):
    """ converts a string of binary into chars that represents each perfix into
        inputs: restorednums, a long srting of binary numbers
                keysdict: a dict with keys (perfixes) referring to the corresponding chars
        output: decoded text
    """
    output =""
    counter = 1
    while restorednums != "":
        if restorednums[0:counter] in keysdict:    
            output+=keysdict[restorednums[0:counter]]
            restorednums = restorednums[counter:]
            counter = 1
        else:
            counter+=1
    return output
