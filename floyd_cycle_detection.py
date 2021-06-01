def floyd_cycle_detect(arr):
    """
    floyd cycle detection use two pointers: one slow, one fast
    eventually two pointers met at the entrance of the circle
    input: arr with positive integers and only one integers are repeated, all others are distinct
    output: find the repeated integer
    Here we use an array of integers to simulate the graph nodes: 
    for example [2, 5, 9, 6, 9, 3, 8, 9, 7, 1] has a cycle start from the index 2
    """
    slow = arr[0]
    fast = arr[arr[0]]
    # will eventually met because fast is two times faster than slow
    # 2(x1 + a) = fast steps
    # x1 + a = slow steps
    # 2(x1 + a) = x1 + a + nC #here nC means n cycles fast pointer made before met slow
    while slow != fast:
        slow = arr[slow]
        fast = arr[arr[fast]]

    # once they met, let slow start from the beginning
    slow = 0
    #this time they walk at the same speed
    # when slow walks x1 steps: x1 = nC - a = (n-1)C + C-a which is the entrance of the cycle
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]
    return slow



if __name__ == "__main__":
    arr = [2, 5, 9, 6, 9, 3, 8, 9, 7, 1]
    print(floyd_cycle_detect(arr))


    
