"""
arr = [10, 8, 2, 3, 1, 4]
n = 6
output = [1, 2, 3, 4, 8, 10]

Time complexirt =O(n**2)
aux space = O(1)
total space = O(n)
"""

def selection_sort(arr, n):
    for i in range(n-1):
        index = i
        for j in range(i+1, n):
            if arr[j]< arr[index]:
                index = j
        arr[index], arr[i] = arr[i], arr[index]
    return arr


arr = [10, 8, 2, 3, 1, 4]
n = len(arr)
print(selection_sort(arr, n))