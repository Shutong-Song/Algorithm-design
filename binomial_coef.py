def binomial_coef_dad(n, k):
    """
    divide-and-conquer which repeated calculated a lot of binomial
    time complexity: each value will split into 2, and we have n of such splits: 2*2*... = O(2^n)
    """
    if n == k or k == 0:
        return 1
    return binomial_coef_dad(n-1, k-1) + binomial_coef_dad(n-1, k)

def binomial_coef(n, k):
    """
    dynamic programming: using a table to store i-1 on range 0 - k values, and used on i
    time complexity: O(nk)
    """
    dp = [1]*(k + 1)
    for i in range(1, n+1):
        prev = 1
        for j in range(1, min(i+1, k+1)):
            if j == i:
                dp[j] = 1
            else:
                prev, dp[j] = dp[j], prev + dp[j]
    return dp[-1]



if __name__ == "__main__":
    n = 15
    k = 5
    res1 = binomial_coef_dad(n, k)
    res2 = binomial_coef(n, k)
    print(res1, res2)