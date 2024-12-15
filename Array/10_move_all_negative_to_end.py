"""
arr = [1, -1, 3, 2, -7, -5, 11, 6]
o/p = [1, 3, 2, 11, 6, -1, -7, -5]
"""

# brutefore
"""
traverse and seggragerate all positive and negative like take an extra array. first add all potive then add all negative
"""

def brute_force(arr):
    temp = []
    for i in arr:
        if i >= 0:
            temp.append(i)
    for i in arr:
        if i < 0:
            temp.append(i)
    return temp


arr = [1, -1, 3, 2, -7, -5, 11, 6]
print(brute_force(arr))