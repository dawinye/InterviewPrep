##https://www.hackerrank.com/challenges/one-month-preparation-kit-caesar-cipher-1/

def caesarCipher(s, k):
    # Write your code here
    newString = ''
    k = k % 26 
    for char in s:
        if ord(char) >= 65 and ord(char) <= 90:
            newChar = ord(char) + k
            if newChar > 90:
                newChar -= 26
            newString += chr(newChar)
        elif ord(char) >= 97 and ord(char) <= 122:
            newChar = ord(char) + k 
            if newChar > 122:
                newChar -=26
            newString += chr(newChar)
        else:
            newString += char
    return newString
