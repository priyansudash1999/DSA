"""
arr = [2, -3, 4, 1, 1, 7]
o/p = 3

Brute force approach 
Time complexity = O(n**2), Space complexity = O(1)

"""

def brute_force(arr, n):
    for i in range(n):
        if i+1 not in arr:
            return i+1
    return -1




arr = [2, -3, 4, 1, 1, 7]
n = len(arr)
print(brute_force(arr, n))



"""
Better approach
Time complexity = O(n), Space complexity = O(1)
"""


def better(arr, n):    
    pass



array = [2, -3, 4, 1, 1, 7]
n = len(array)
print(better(array, n))