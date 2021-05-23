
def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot)
        quick_sort(arr, pivot+1, high)
        
def partition(arr, low, high):
    x = high - 1 
    larger_idx = low - 1
    for i in range(low, high):
        if arr[i] < arr[x]:
            larger_idx += 1
            arr[i], arr[larger_idx] = arr[larger_idx], arr[i]
    arr[x], arr[larger_idx+1] = arr[larger_idx+1], arr[x]
    return larger_idx+1 


if __name__ == "__main__":
    arr = [2, 19, 7, 33, 1, 8, 1]
    low = 0
    high = len(arr)
    quick_sort(arr, low, high)
    print(arr)