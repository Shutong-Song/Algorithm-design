import math as m
from collections import deque

def radix_sort(arr):
    max_digits = 0
    for val in arr:
        if max_digits < m.ceil(m.log10(val)):
            max_digits = m.ceil(m.log10(val))
    
    bucket = [deque() for _ in range(10)]
    replace = 1 
    while max_digits:
        for val in arr:
            temp = val//replace
            bucket[temp%10].append(val)
            
        i = 0
        for val in bucket:
            while val:
                arr[i] = val.popleft()
                i += 1
        max_digits -= 1
        replace *= 10


if __name__ == "__main__":
    arr = [2, 19, 7, 33, 1, 8, 1]
    arr1 = [1, 2, 3, 4]
    arr2 = [4, 3, 2, 1]
    radix_sort(arr2)
    print(arr2)
    
