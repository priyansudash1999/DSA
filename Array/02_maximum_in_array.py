# brute force
"""
time complexity and space complexity are O(nlogn) and O(1) respectively
"""

def maximum_in_array(arr):
    arr.sort()
    return arr[-1]



arr = [2, 1, 3, -1, 7]
res = maximum_in_array(arr)
print(res)


# Optimal
"""
time complexity and space complexity are O(n) and O(1) respectively
"""

def optimal(array):
    max_ = array[0]
    for i in range(len(array)):
        if array[i] > max_:
            max_ = array[i]

    return max_


array = [2, 9, 0, 1, -1, -7]
print(optimal(array))