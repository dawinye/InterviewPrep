##https://www.hackerrank.com/challenges/one-month-preparation-kit-drawing-book/

def pageCount(n, p):
    # Write your code here
    fromFront = math.ceil((p-1)/2)
    if n % 2 == 0:
        if n != p:
            fromBack = math.floor((n-1-p)/2) + 1
        else:
            return 0
    else:
        fromBack = math.floor((n-p)/2)
    return min(fromFront,fromBack)
