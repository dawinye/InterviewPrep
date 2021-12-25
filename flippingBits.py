##https://www.hackerrank.com/challenges/one-month-preparation-kit-flipping-bits/

def flippingBits(n):
    # Write your code here
    binaryN = bin(n).replace("0b","")
    if len(binaryN) < 32:
        filler = 32 - len(binaryN)
        binaryN = filler * "0" + binaryN
    newString = ""
    for char in binaryN:
        if char == '1':
            newString += "0"
        else:
            newString += '1'
    
    return int(newString,2)
