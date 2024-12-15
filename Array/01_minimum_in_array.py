# brute force
"""
time complexity and space complexity are O(nlogn) and O(1) respectively
"""

def minimum_in_array(arr):
    arr.sort()
    return arr[0]



arr = [2, 1, 3, -1, 7]
res = minimum_in_array(arr)
print(res)


# Optimal
"""
time complexity and space complexity are O(n) and O(1) respectively
"""

def optimal(array):
    min_ = array[0]
    for i in range(len(array)):
        if array[i] < min_:
            min_ = array[i]

    return min_


array = [2, 9, 0, 1, -1, -7]
print(optimal(array))