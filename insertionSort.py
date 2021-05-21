# insertion sort
def insertion_sort(arr):
    """
    keep comparing with the sorted deck, and place the new element in the right place
    time complexity: worst-case O(n^2), best-case O(n)
    """
    for idx in range(len(arr)):
        key = arr[idx]
        k = idx - 1
        while k > - 1 and key < arr[k]:
            arr[k+1] = arr[k]
            k -= 1
        key, arr[k+1] = arr[k+1], key
    return arr


if __name__ == "__main__":
    arr = [12, 3, 12, 17, 33, 9]
    arr1 = [2, 19, 7, 33, 1, 8, 1]
    arr2 = [1, 2, 3, 4]
    arr3 = [4, 3, 2, 1]
    print(insertion_sort(arr))
