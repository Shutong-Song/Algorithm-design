## binary search using divide-and-conquer


def binary_search(arr, elem, low, high):
    """
    binary search using divide-and-conquer
    time complexity: O(log(n)) where n is the length of arr
    """
    while low < high:
        mid = (low + high)//2
        if arr[mid] == elem:
            return mid
        elif arr[mid] > elem:
            high = mid
        else:
            low = mid + 1
    return -1



def binary_search_recur(arr, elem, low, high):
    """
    binary search using recursive approach
    time complexity: O(log(n))
    """
    if low >= high:
        return -1
    mid = (low + high)//2
    if arr[mid] == elem:
        return mid
    elif arr[mid] > elem:
        return binary_search_recur(arr, elem, low, mid)
    else:
        return binary_search_recur(arr, elem, mid+1, high)
            

## application 1: find the peak element of an array
## find the element that greater than its left and right neighbors
## example: arr = [1, 2, 1, 3, 5, 6, 4], the index of peak element is either 1 (element 2) or 5 (element 6)
## any conjunct elements are different: arr[i] != arr[i + 1]
def peak_element_iter(arr):
    """
    keep find the middle element, compare it to its right side, 
                       if arr(mid) > arr(mid + 1), let start_index = mid + 1
                       else let end_index = mid
    output: the index of the peak element, if there are multiple peak element, randomly return one
    """
    low = 0
    high = len(arr) - 1
    while low < high:
        mid = (low + high)//2
        if arr[mid] < arr[mid + 1]:
            low = mid + 1
        else:
            high = mid
    return low

def peak_element_recur(arr, low, high):
    """
    recursive way of peak_element_iter() function
    output: index
    """
    if low == high:
        return low
    mid = (low + high)//2
    if arr[mid] < arr[mid + 1]:
        return peak_element_recur(arr, mid + 1, high)
    return peak_element_recur(arr, low, mid)


## binary search for 2D matrix: every row is sorted ascending order, every column is in ascending order
## find the target element, if no such element, return INF, else return the index
def binary_search_2d_iter(mat, target):
    """
    find the row index and column index of a matrix that equals to the target, if no such element, return INF
    output: row index, columns index if target is in the matrix
    """
    low_r = 0
    high_r = len(mat) - 1
    c = len(mat[0]) - 1
    while low_r < high_r:
        mid_r = low_r + (high_r - low_r)//2
        if mat[mid_r][c] == target:
            return (mid_r, c)
        elif mat[mid_r][c] > target:
            high_r = mid_r
        else:
            low_r = mid_r + 1
    low_c = 0
    high_c = len(mat[0])
    while low_c < high_c:
        mid_c = (high_c + low_c)//2
        if mat[low_r][mid_c] == target:
            return (low_r, mid_c)
        elif mat[low_r][mid_c] > target:
            high_c = mid_c
        else:
            low_c = mid_c + 1

    return float("inf")




if __name__ == "__main__":
    arr = [1, 8, 12, 21, 33, 45, 90]
    arr = [1, 2, 1, 3, 5, 6, 4]
    arr = [1, 2, 3, 1]
    arr1 = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]  
    x1 = 3
    arr2 = [[2, 4, 9, 14, 14, 15, 18],[21, 27, 31, 35, 42, 45, 50],[54, 59, 64, 69, 82, 84, 84]]
    x2= 18 
    arr3 = [[3, 15, 21, 24, 83, 87, 88, 93],[178, 319, 541, 669, 770, 793, 848, 970], [1439, 1546, 1853, 2124, 2234, 2459, 2518, 2978], [3111, 3406, 3490, 3669, 3796, 3936, 4112, 4776],[5277, 5667, 6067, 6555, 7890, 8056, 8234, 9968]]
    x3 = 970 
    #binary_search_recur(arr, elem, 0, len(arr))
    #res = peak_element_iter(arr)
    #res = peak_element_recur(arr, 0, len(arr) - 1)
    for mat, target in zip([arr1, arr2, arr3], [x1, x2, x3]):
        res = binary_search_2d_iter(mat, target)
        print(res)
        print("\n")