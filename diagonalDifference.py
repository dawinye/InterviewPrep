##https://www.hackerrank.com/challenges/one-month-preparation-kit-diagonal-difference/

def diagonalDifference(arr):
    # Write your code here
    numOfColumns = len(arr[0])
    
    firstDiag = 0
    firstDiagPointer = 0
    secondDiagPointer = numOfColumns - 1
    secondDiag = 0
    
    for i in range(0,len(arr)):
        firstDiag += arr[i][firstDiagPointer]
        firstDiagPointer += 1
        secondDiag += arr[i][secondDiagPointer]
        secondDiagPointer -= 1
    return abs(firstDiag-secondDiag)
