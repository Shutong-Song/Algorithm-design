
def merge_sort(arr, low, high):
    """
    divide-and-conquer to keep divide the array into small subarray, then merge() function will merge them
    time complexity: worst-case and best-case both are O(nlg(n))
    """
    if low < high - 1:
        mid = (low + high)//2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid, high)
        merge(arr, low, mid, high)
        
def merge(arr, low, mid, high):
    L = arr[low:mid]
    R = arr[mid:high]
    i = j = 0
    k = low
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1 
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
        
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

if __name__ == "__main__":
    arr = [12, 3, 12, 17, 33, 9]
    arr1 = [2, 19, 7, 33, 1, 8, 1]
    arr2 = [1, 2, 3, 4]
    arr3 = [4, 3, 2, 1]
    low = 0
    high = len(arr)
    merge_sort(arr, low, high)
    print(arr)