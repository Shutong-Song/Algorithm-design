def selection_sort(arr):
    """
    keep finding the smallest element index during the running against the second loop,
    and keep placing it in front of rest larger elements 
    time complexity: worst-case O(n^2), best-case O(n^2)
    """
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]
    return arr


if __name__ == "__main__":
    arr = [12, 3, 12, 17, 33, 9]
    arr1 = [2, 19, 7, 33, 1, 8, 1]
    arr2 = [1, 2, 3, 4]
    arr3 = [4, 3, 2, 1]
    print(selection_sort(arr))