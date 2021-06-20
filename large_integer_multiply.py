### Ala carte large integers multiplication
### rectangle large integers multiplication

def Ala_Carte(num1,num2):
    """
    assume num1 is bigger, num1 keeps integer dividing 2, num2 keeps multiplying 2, 
    if num1 is odd, store corresponding num2 in a list, finally sum the list when nums1 == 0
    time complexity: O(log(num1))
    """
    sign = "pos" if (num1>0 and num2>0) or (num1 <0 and num2 <0) else "neg"
    odd_elements = []
    num1 = abs(num1)
    num2 = abs(num2)
    while num1//2:
        if num1%2 == 1:
            odd_elements.append(num2)
        num1 = num1//2
        num2 = num2*2
    odd_elements.append(num2)
    return sum(odd_elements) if sign=="pos" else -sum(odd_elements)

def rect_mul(num1, num2):
    """
    rectangle multiplication
    """
    num1_arr = []
    num2_arr = []
    sign = "pos" if (num1>0 and num2>0) or (num1 <0 and num2 <0) else "neg"
    num1 = abs(num1)
    num2 = abs(num2)
    while num1:
        num1_arr.append(num1%10)
        num1 = num1//10
    while num2:
        num2_arr.append(num2%10)
        num2 = num2//10
   
    carry = []
    arr_len = len(num1_arr) + len(num2_arr) - 1
    arrs = [[] for x in range(len(num1_arr))]
    for i,val1 in enumerate(num1_arr):
        carry_temp = 0
        arrs[i] = [0]*i
        for val2 in num2_arr:
            arrs[i].append((val1*val2)%10+carry_temp)
            carry_temp = (val1*val2)//10
        if len(carry):
            arrs[i][-1] = arrs[i][-1]+carry.pop()
        arrs[i] = arrs[i] + [0]*(arr_len-len(arrs[i]))
        if carry_temp:
            carry.append(carry_temp)
            
    carry_last = 0
    res_digits = [0]*arr_len
    for i in range(arr_len):
        for arr in arrs:
            res_digits[i] += arr[i]
        res_digits[i] += carry_last
        carry_last = res_digits[i]//10
        res_digits[i] %= 10
    if len(carry):
        carry_last += carry.pop()
    if carry_last//10:
        res_digits.append(carry_last%10)
        res_digits.append(carry_last//10)
    elif carry_last%10:
        res_digits.append(carry_last)
        
    res = 0
    for i, val in enumerate(res_digits):
        res += val*(10**i)
    return res if sign == "pos" else -res

if __name__ == "__main__":
    test1 = (7000, 7294)
    test2 = (25, 5038385)
    test3 = (-59724,783)
    test4 = (8516,-82147953548159344)
    test5 = (45952456856498465985, 98654651986546519856)
    test6 = (-45952456856498465985, -98654651986546519856)
    for i, (num1,num2) in enumerate([test1,test2, test3, test4, test5, test6]):
        print("test case "+str(i+1)+":")
        print(Ala_Carte(num1,num2))
        print("\n")