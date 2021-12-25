##https://www.hackerrank.com/challenges/one-month-preparation-kit-pangrams/

def pangrams(s):
    # Write your code here
    letters = set()
    s = s.lower()
    s = s.replace(" ","")
    for char in s:
        if char not in letters:
            letters.add(char)
            
    if len(letters) == 26:
        return "pangram"
    else:
        return "not pangram"
