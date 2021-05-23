def counting_sort(arr):
    res = [0]*len(arr)
    if not arr:
        return []
    max_elem = max(arr)
    temp = [0]*(max_elem + 1)
    for val in arr:
        temp[val] += 1
    for i in range(1, len(temp)):
        temp[i] += temp[i-1]
    for i in range(len(arr)-1, -1, -1):
        res[temp[arr[i]] - 1] = arr[i]
        temp[arr[i]] -= 1
    return res

if __name__ == "__main__":
    arr = [2, 19, 7, 33, 1, 8, 1]
    arr1 = [1, 2]
    arr2 = [4, 3, 2, 1]
    print(counting_sort(arr2))