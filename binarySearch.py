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
    if low < high:
        mid = (low + high)//2
        if arr[mid] == elem:
            return mid
        elif arr[mid] > elem:
            return binary_search_recur(arr, elem, low, mid)
        else:
            return binary_search_recur(arr, elem, mid+1, high)


if __name__ == "__main__":
    arr = [1, 8, 12, 21, 33, 45, 90]
    elem =  90 
    res = binary_search_recur(arr, elem, 0, len(arr))
    print(res)