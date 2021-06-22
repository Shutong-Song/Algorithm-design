def find_kth(arr, k, low, high):
    """
    find the kth smallest element in an array using partition
    input: an array with start index and end index are low, high - 1, a integer k
    output: the kth smallest element in the array
    average-case time complexity: O(n) where n is the length of arr
    space complexity: O(1)
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


## find the kth largest element in an array works similar when using partition
## we can also use priority queue, keep pop the largest until we popped k - 1 largest element, 
#      then, the first element left in the arr is the kth largest
def find_kth_largest(arr, k):
    """
    time complexity: O(n + k*log(n)) where n is the length of the arr
    space complexity: O(n)
    """
    import heapq #python heapq is a min-heap which the smallest element has the highest priority (pop first)
    nums = [-x for x in arr] #make sure the largest will be popped first
    heapq.heapify(nums)  # average time complexity O(n)
    i = 0
    while i < k - 1:
        heapq.heappop(nums) #pop k times: k*log(n)
        i += 1
    return - nums[0] 


if __name__ == "__main__":
    arr = [1, 9, 7, 13, 2, 8, 8, 6]
    print(find_kth_largest(arr, 8))
