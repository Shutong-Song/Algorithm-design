
from countingSort import counting_sort

def bucket_sort(arr, factor = 100):
    bucket = 10
    res = [[] for _ in range(bucket)]
    arr = [x/factor for x in arr]
    for val in arr:
        res[int(bucket*val)].append(int(val*factor))
    for i in range(len(res)):
        i
        res[i] = counting_sort(res[i])
    x = []
    for b in res:
        x.extend(b)
    return x


if __name__ == "__main__":
    arr = [12, 3, 12, 17, 33, 9]
    arr1 = [78, 17, 39, 26, 72, 94, 21, 12, 23, 68]
    print(bucket_sort(arr1))
