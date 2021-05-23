def heap_sort(arr):
    """
    use max heap to sort
    """
    for i in range(len(arr)//2-1, -1, -1):
        heapify(arr, i, len(arr))
    for j in range(len(arr)-1, 0, -1):
        arr[j], arr[0] = arr[0], arr[j]
        heapify(arr, 0, j)

def heapify(arr, i, arr_len):
    left = 2*i + 1
    right = 2*i + 2
    largest = i
    if left < arr_len and arr[left] > arr[largest]:
        largest = left
    if right < arr_len and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        heapify(arr, largest, arr_len)
    
def minheap_sort(arr):
    """
    use min heap to sort, need reverse the sorted list at the end
    """
    for i in range(len(arr)//2-1, -1, -1):
        min_heapify(arr, i, len(arr))
    for j in range(len(arr)-1, 0, -1):
        arr[j], arr[0] = arr[0], arr[j]
        min_heapify(arr, 0, j)
    return arr[::-1]

def min_heapify(arr, i, arr_len):
    left = 2*i + 1
    right = 2*i + 2
    smallest = i
    if left < arr_len and arr[left] < arr[smallest]:
        smallest = left
    if right < arr_len and arr[right] < arr[smallest]:
        smallest = right
    if smallest != i:
        arr[smallest], arr[i] = arr[i], arr[smallest]
        min_heapify(arr, smallest, arr_len)
    

if __name__ == "__main__":
    arr = [2, 19, 7, 33, 1, 8, 1]
    heap_sort(arr)
    print(arr)