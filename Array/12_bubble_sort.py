"""
arr = [7, 4, 8, 5, 3]
output = [3,4,5,7,8]
"""

def bubble_sort(arr, n):
    for i in range(n-2, -1, -1):
        for j in range(0, i+1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


arr = [7, 4, 8, 5, 3]
n = len(arr)    
print(bubble_sort(arr, n))  