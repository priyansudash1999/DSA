"""
arr = [2, -3, 4, 1, 1, 7]
o/p = 3


"""

def brute_force(arr, n):
    for i in range(n):
        if i+1 not in arr:
            return i+1
    return -1




arr = [2, -3, 4, 1, 1, 7]
n = len(arr)
print(brute_force(arr, n))