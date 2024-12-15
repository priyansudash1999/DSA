"""
arr  = [2, 7, 4, 11, 5, 8]
o/p = [8, 2, 7, 4, 11, 5]
"""

# Brute force approach

"""
time complexity = O(n), space complexity = O(n)
"""

def better(arr, n):
    temp  =arr[-1]
    for i in range(n-2, -1, -1):
        arr[i+1] = arr[i]
    arr[0] = temp
    return arr

arr = [2, 7, 4, 11, 5, 8]
n = len(arr)
print(better(arr, n))