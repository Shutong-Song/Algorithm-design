### find the maximum summation of a continuous subarray of an array


# 1. use dynamic programming if only need return the max sum
# this algorithm is Kadane's algorithm
def maxsum_dp(arr):
    """
    output the maximum summation of the subarray
    time complexity: O(n)
    """
    global_max = float("-inf")
    local_max = 0
    for num in arr:
        local_max = max(local_max + num, num) #need local_max store the current maximum
        if local_max > global_max:
            global_max = local_max
    return global_max

# 2. dynamic programming with return the subarray's start and end index
def maxsub_dp(arr):
    """
    arr is an array with integer elements
    output: total sum, the beginning and end index in arr
    time complexity: O(n)
    """
    optimal = float("-inf")
    temp_max = 0
    left = 0
    right = 0
    temp_left = 0

    for idx, num in enumerate(arr):
        temp_max = max(temp_max + num, num)
        if temp_max == num:
            temp_left = idx
        if temp_max > optimal:
            optimal = temp_max
            right = idx
            left = temp_left
    return optimal, left, right


# 3. we can also solve this using divide-and-conquer
def maxsub_dac(arr, low, high):
    """
    divide-and-conquer with time complexity: O(nlog(n))
    input: arr, the start index of arr, and the length of arr
    output: the total max sum of the subarray, the start and end index of the subarray in the arr
    """
    if low + 1 == high:
        return arr[low], low, low + 1
    
    mid = (low + high)//2
    left_sum, left_low, right_low = maxsub_dac(arr, low, mid)
    right_sum, left_high, right_high = maxsub_dac(arr, mid, high)
    cross_sum, left_cross, right_cross = cross_maxsub(arr, low, mid, high)
    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_sum, left_low, right_low
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_sum, left_high, right_high
    else:
        return cross_sum, left_cross, right_cross

def cross_maxsub(arr, low, mid, high):
    left_sum = float("-inf") 
    temp_sum = 0
    for i in range(mid-1, low-1, -1):
        temp_sum += arr[i]
        if temp_sum > left_sum:
            left_sum = temp_sum
            left = i

    right_sum = float("-inf") 
    temp_sum = 0

    for i in range(mid, high):
        temp_sum += arr[i]
        if temp_sum > right_sum:
            right_sum = temp_sum
            right = i
    return left_sum + right_sum, left, right


# 4. divide-and-conquer if we only need return the max sum
def maxsub_dac1(arr, low, high):
    if low == high - 1:
        return arr[low]
    #elif low == high:
    #    return float("-inf")
    
    mid = (low + high)//2
    lmax = maxsub_dac1(arr, low, mid)
    rmax = maxsub_dac1(arr, mid, high)

    left_sum = float("-inf")
    temp_sum = 0
    for i in range(mid-1, low-1, -1):
        temp_sum += arr[i]
        left_sum = max(temp_sum, left_sum)

    right_sum = float("-inf")
    temp_sum = 0
    for i in range(mid, high):
        temp_sum += arr[i]
        right_sum = max(temp_sum, right_sum)
    return max(max(rmax, lmax), left_sum + right_sum)



# 5. brute-force to try all subarrays, time complexity: O(n^2) where n is the length of arr
def maxsub_brute(arr):
    """
    input: arr
    output: the maximum sum of the subarray, start and end index of the subarray in the arr
    """
    global_max = float("-inf")
    left = 0
    right = 0
    for i in range(len(arr)):
        temp_max = 0
        for j in range(i, len(arr)):
            temp_max += arr[j]
            if temp_max > global_max:
                global_max = temp_max
                left = i
                right = j
    return global_max, left, right


if __name__ == "__main__":
    arr = [-1, -2]
    #arr = [31,-41,59,26,-53,58,97,-93,-23,84]
    #arr = [8, -19, 5, -4, 20]
    res1 = maxsum_dp(arr)
    res2 = maxsub_dp(arr)
    res3 = maxsub_dac(arr, 0, len(arr))
    res4 = maxsub_dac1(arr, 0, len(arr))
    res5 = maxsub_brute(arr)
    print(res4)


        