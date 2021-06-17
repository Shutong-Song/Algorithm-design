### Boyer-Moore majority voting algorithms


def majority(arr):
    """
    majority element in an array is an element with occurrence > len(arr)//2
    time complexity: O(n) where n is the length of arr
    space complexity: O(1)
    """
    cnt = 0
    major = 0
    for val in arr:
        # if cnt == 0, reassign major element
        # check cnt pointer, it is either increase by 1 or decrease by 1 each time in the loop
        if cnt == 0:
            major = val
        cnt += 1 if major == val else -1
    return major 


# one application is to find all majority elements that is > len(arr)//k
# for example: find all elements in arr that > len(arr)//3, 
# maximum number of elements have occurrence > one-third are 2
        
def majority_three(arr):
    major1, major2 = 0, 1
    cnt1, cnt2 = 0, 0
    for val in arr:
        if major1 == val:
            cnt1 += 1
        elif major2 == val:
            cnt2 += 1
        elif cnt1 == 0:
            major1 = val
        elif cnt2 == 0:
            major2 = val
        else:
            cnt1 -= 1
            cnt2 -= 1
    return [val for val in [major1, major2] if arr.count(val) > len(arr)//3]