def min_max_arr(arr):
    """
    implement min_max detection for an array with 3*floor(n/2) comparison
    """
    n = len(arr)
    max_elem = min_elem = 0
    if n == 0:
        return (None, None)
    if n == 1:
        max_elem = min_elem = arr[0]
        return (max_elem, min_elem)
    if n%2 == 0:
        max_elem = arr[0] if arr[0] > arr[1] else arr[1]
        min_elem = arr[0] if arr[0] < arr[1] else arr[1]
    else:
        max_elem = min_elem = arr[0]
    
    for i in range(3 if n%2 == 0 else 2, n, 2):
        if arr[i] > arr[i-1]:
            max_elem = arr[i] if arr[i] > max_elem else max_elem
            min_elem = arr[i-1] if arr[i-1] < min_elem else min_elem
        else:
            min_elem = arr[i] if arr[i] < min_elem else min_elem
            max_elem = arr[i-1] if arr[i-1] > max_elem else max_elem
            
    return (max_elem, min_elem)

if __name__ == "__main__":
    arr = [3, 17, 29, 1, 66, 66]
    arr = []
    arr = [1]
    arr = [3, 3, 3, 3]
    m, n = min_max_arr(arr)
    print(m, n)

