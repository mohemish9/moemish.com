def compress():
    """compress compresses a given file
       input: N/A, user input
       output: N/A, compressed file and key file
    """
    inputfile = input("Enter a file to compress:")
    f1 = open(inputfile, "r")
    text = f1.read()
    f1.close()
    frequencies = frequency(text)
    hufftree = maketree(frequencies)
    prefixs = makeprefix(hufftree)
    prefixsdict = makeDict(prefixs)
    encodedtext= encode(text,prefixsdict)
    bitslist = makebits(encodedtext)
    outputfiles(inputfile, prefixsdict, bitslist, len(encodedtext))
    print("Original file:" + inputfile)
    print("Distinct characters:" + str(len(prefixsdict)))
    print("Total bytes:" + str(len(text)))
    print("Compressed text length in bytes:" + str(len(bitslist)))
    print("Asymptotic compression ratio:" + str(len(bitslist)/len(text)))


def frequency(text):
    """ frequancy calculates the frequencies of different chars in a given string
        input: text, a string 
        output: a dictionary which its keys are different chars in the input string and they each key refares to the frequancy of its presence
    """
    count = {}
    for char in range(len(text)):
        if tuple(text[char]) in count:
            count[tuple(text[char])] += 1/len(text)
        else:
            count[tuple(text[char])] = 1/len(text)
    return count


def maketree(frequencies):
    """Returns a tuple representing the Huffman tree for the given frequency dictionary. """
    while len(frequencies) >= 2:
        low1 = minfrequency(frequencies)
        freq1 = frequencies[low1]
        del frequencies[low1]
        low2 = minfrequency(frequencies)
        freq2 = frequencies[low2]
        del frequencies[low2]
        frequencies[(low1, low2)] = freq1 + freq2
    return list(frequencies.keys())[0]

import math
def minfrequency(frequencies):
    """ returns the minimum value refared to in a dict
    """
    minkey = ''
    minvalue = math.inf
    for x in frequencies:
        if frequencies[x] < minvalue:
            minvalue = frequencies[x]
            minkey = x
    return minkey

def makeprefix(tree):
    """ returns the prefix of every char in a given huffman tree
        input: tree, a tuple representing huffman tree
        output: a list of tuples each of which contains a char and its prefix
    """
    if len(tree) == 1:
        return [(tree,"")]
    else:
        left, right = tree
        l = makeprefix(left)
        r = makeprefix(right)
        leftresult = []
        rightresult = []
        for x in l:
            leftresult.append((x[0][0], "0"+ x[1]))
        for y in r:
            rightresult. append((y[0][0], "1"+ y[1]))
    return leftresult+rightresult

def makeDict(prefixslist):
    """converts a list of prefixes into a dict
        input: prefixlist, a list of tuples each of which contains a char and its prefix
        output: a dict with the chars as keys refering to their prefixes
    """
    dictionary = {}
    for x in prefixslist:
        dictionary[x[0]] = x[1]
    return dictionary

def encode(text, prefixsdict):
    """converts every char in a given string into prefixes (0s and 1s)
        input: text, string desired to be converted
               prefixsdict, dict containg every char in text that refares to the prefix of this char
        output: a long string of 0s abd 1s that represents the prefixes of the original number
    """
    output= ""
    for x in text:
        output+= prefixsdict[x]
    return output

def makebits(string):
    """ chunks a given string of 0s and 1s into 8-bit number
        input: string, a long string of 0s and 1s
        output: a list of 8-bits numbers that represents 8-bit chucks of the input string
    """
    output=[]
    while len(string)>8:
        number = BinaryToNum(string[:8])
        output.append(number)
        string = string[8:]
    if len(string) != 0:
        number = BinaryToNum(string)
        output.append(number)
    return output

def BinaryToNum(string):
    """ converts binary number to 8-bit number
        input: string, an 8-bit long binary number
        output: 8-bit number representing the input
    """
    answer = 0
    for x in string:
        answer = answer * 2
        if x == "1":
            answer = answer + 1
    return answer

def outputfiles(filename, prefixsdict, bitslist, reallen):
    """writes the .HUFFMAN and .HUFFMAN.KEY files
      inputs: filename, user input name
              prefixsdict, dict containing the converstion prefix of each char (contians of the .HUFFMAN.KEY file)
              bitslist, the 8-bit represention of the original file (contiant of the .HUFFMAN file)
              reallen, the length of the 0s and 1s string (required to ditermine the number of zeros added by EightBitsNumToBinary that doesn't belong to the original string)
     output: N/A, writes the two new files
    """
    f2 = open(filename+".HUFFMAN.KEY", "w")
    f2.write(str(reallen) + "\n" +
             str(len(prefixsdict)) + "\n"+
             str(len(bitslist))    +  "\n") # I added reallen to this file bec I think i need it for my code to work!
    for key in prefixsdict:
        f2.write(key+prefixsdict[key]+"\n")
    f2.close()
    f3= open(filename+".HUFFMAN", "wb")
    f3.write(bytes(bitslist))
    f3.close()

