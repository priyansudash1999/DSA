"""
array = [2, 4, 6, 3, 8, 5, 1]
output:- 6

"""

# Bruteforce
"""
time complexity = O(nlogn)
space complexity = O(1)
"""

def sec_max(array):
    array.sort()
    return array[-2]


array = [2, 4, 6, 3, 8, 5, 1]
print(sec_max(array))

# Better
"""

"""

def sec_max_better(arr):
    max_ = arr[0]
    for i in range(len(arr)):
        if arr[i] > max_:
            max_ = arr[i]
    sec_max_ = arr[0]
    for j in range(len(arr)):
        if arr[j] != max_:
            if arr[j] > sec_max_:
                sec_max_ = arr[j]
    return sec_max_



arr = [8,8,8,8,8,8,8,8]
print(sec_max_better(arr))