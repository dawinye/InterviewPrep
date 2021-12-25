##https://www.hackerrank.com/challenges/one-month-preparation-kit-countingsort1/

def countingSort(arr):
    # Write your code here
    result = [0] * 100
    
    for element in arr:
        result[element] += 1
    
    return result
