"""

arr = [1, 3, 4, 5, 6]
o/p = 2

Brute force approach

time complexity = O(n**2)
space complexity = O(1)

"""

def brute_force(arr):
    for i in range(len(arr)):
        if i+1 not in arr:
            return i+1


arr= [1, 3, 5, 6, 4]
print(brute_force(arr))


"""

Better approach


"""

def better(array):
    sum1 = 0
    sum2 =0
    n = len(array)
    for i in range(n-1):
        sum2 += array[i]
    sum1 = n*(n+1)//2
    return sum1-sum2

array = [1, 3, 4, 5, 6]
print(better(array))
