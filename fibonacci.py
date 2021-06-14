
#1. calculate fibonacci number
def calc_fibo(n):
    """
    dynamic programming: time complexity O(n)
    """
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

#1. calculate the last digit of a fibonacci number
def calc_fibo_last_digit(n):
    """
    dynamic programming: save only the last digit of calculated fibonacci number
    """
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(n):
        a, b = b%10, (a + b)%10
    return a

if __name__ == "__main__":
    fi = calc_fibo_last_digit(24)
    print(fi)
    