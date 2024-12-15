"""
arr = [2, 5, 4, 3, 1]
o/p = [1, 3, 4, 5, 2]
"""

# Brute-force
"""
time complexity = O(n), space compelxity = O(n)
"""

def reverse_an_array(arr):
    array = []
    for i in range(len(arr)-1, -1, -1):
        array.append(arr[i])
    return array

arr = [2, 5, 4, 3, 1]
print(reverse_an_array(arr))


# optimal
"""
time complexity = O(n), space complexity = O(1)
"""

def reverse(array):
    i = 0
    j = len(array)-1
    while i <= j:
        array[i], array[j] = array[j], array[i]
        i+=1
        j-=1
    return array

array = [2, 5, 4, 3, 1]
print(reverse(array))