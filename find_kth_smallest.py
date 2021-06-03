def find_kth(arr, k, low, high):
    """
    find the kth smallest element in an array using partition
    input: an array with start index and end index are low, high - 1, a integer k
    ouput: the kth smallest element in the array
    """
    if low == high -1:
        return arr[low]
    q = partition(arr, low, high)
    pos = q - low + 1
    if pos == k:
        return arr[q]
    elif pos > k:
        return find_kth(arr, k, low, q)
    return find_kth(arr, k - pos, q+1, high)

def partition(arr, low, high):
    """
    partition an array into two parts, left element are all smaller than pivot_val, right are larger
    input:
    output: the index of the pivot element
    """
    pivot_val = arr[low]
    p_larger = low
    for i in range(low+1, high):
        if arr[i] < pivot_val:
            p_larger += 1
            arr[i], arr[p_larger] = arr[p_larger], arr[i]
    arr[p_larger], arr[low] = arr[low], arr[p_larger]
    return p_larger


if __name__ == "__main__":
    arr = [1, 9, 7, 13, 2, 8, 8, 6]
    print(find_kth(arr, 8, 0, len(arr)))
