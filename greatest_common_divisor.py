###

# 1. greatest common divisor of two integers: for a = 20, b = 15, the gcd is 5
def gcd_naive(a, b):
    """
    naive method for find the greatest common divisor that can divide both a and b
    time complexity: O(a + b)
    """
    best = 0
    for i in range(1, a + b):
        if a%i == 0 and b%i == 0:
            best = i
    return best

# 2. GCD using Euclidean theory
def gcd_euclidean(a, b):
    """
    constantly module the smaller integer b, and change the position of (b, a%b) so bigger integer always first input arg
    time complexity: O(log(a*b))
    """
    if b == 0:
        return a
    return gcd_euclidean(b, a%b)



### least_common_multiple(a, b) = abs(a*b)/GCD(a, b)


if __name__ == "__main__":
    a = 28851538
    b = 1183019
    best_gcd = gcd_euclidean(a, b)
    print(best_gcd)
    print("least_common_multiplier", a*b//best_gcd)
