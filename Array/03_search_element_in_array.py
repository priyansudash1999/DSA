"""
time complexity = O(n), space complexity = O(1)
"""

def search(arr, ele):
    for i in range(len(arr)):
        if arr[i] == ele:
            return i
    return -1

arr = [19, 10, 7, 11, 8, 4]
target = 8
print(search(arr, target))