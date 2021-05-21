
def bubble_sort(arr):
    """
    keep comparing the two adjacent elements in the inner loop, and the outer loop make the inner comparison repeat n times
    time complexity: worst-case
    """
    for i in range(len(arr)):
        indicator = True 
        for j in range(len(arr)-1, i, -1):
            if arr[j] < arr[j-1]:
                indicator = False
                arr[j], arr[j-1] = arr[j-1], arr[j]
        if indicator:
            return arr
    return arr

if __name__ == "__main__":
    arr = [12, 3, 12, 17, 33, 9]
    arr1 = [2, 19, 7, 33, 1, 8, 1]
    arr2 = [1, 2, 3, 4]
    arr3 = [4, 3, 2, 1]
    print(bubble_sort(arr))