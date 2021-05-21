
def exchange_sort(arr):
    """
    exchange elements in array: smallest element will placed in the first place when i = 0, then second smallest when i = 1, etc.
    time complexity: worst-case and best-case both O(n^2)
    """
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


if __name__ == "__main__":
    arr = [12, 3, 12, 17, 33, 9]
    arr1 = [2, 19, 7, 33, 1, 8, 1]
    arr2 = [1, 2, 3, 4]
    arr3 = [4, 3, 2, 1]
    print(exchange_sort(arr))