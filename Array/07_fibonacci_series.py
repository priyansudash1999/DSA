"""

fibonacci  series = 0,1,1,2,3,5,8,13,21,...


"""

def fibonacci(arr, n):
    arr[0] = 0
    arr[1] = 1
    for i in range(2, n):
        arr[i] = arr[i-1] + arr[i-2]
    return arr


n = 18
arr = [0]*n
print(fibonacci(arr, n))
