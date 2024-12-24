def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
               break
    return arr
         

arr = [9, 1, 3, 2, 4]
print(insertion_sort(arr))