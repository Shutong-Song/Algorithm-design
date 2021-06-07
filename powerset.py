
def powerset(arr):
    res = []
    solve_powerset(0, arr, [], res)
    return res

def solve_powerset(cur, arr, temp, res):
    res.append(temp)
    if cur < len(arr):
        for i in range(cur, len(arr)):
            solve_powerset(i+1, arr, temp + [arr[i]], res)


if __name__ == "__main__":
    arr = [1, 3, 5]
    arr = [2, 2, 3]
    res = powerset(arr)
    print(res)
