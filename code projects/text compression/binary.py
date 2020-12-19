def EightBitNumToBinary(num):
    output = ""
    while num > 0:
        if num % 2 == 0:
            output = "0" + output
        else:
            output = "1" + output
        num = int(num/2)
    padding = 8 - len(output)
    return padding * "0" + output

def BinaryToNum(string):
    answer = 0
    for x in string:
        answer = answer * 2
        if x == "1":
            answer = answer + 1
    return answer
