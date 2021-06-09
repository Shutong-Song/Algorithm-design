# rod cut problem in CLRS: to maximize the profit of cut a length n rod with a price table
# the price table has index as length of rod, and value with corresponding price


def cut_rod_dad(n, price_table):
    """
    use divide-and-conquer: top-down approach
    this is no dynamic programming ways to solve rod cut problem, use divide-and-conquer(dad)
    previous best result will not be saved, so the recusive approach will have a lot of repeated calculations
    """
    if n == 0:
        return 0
    q = 0
    for i in range(1, n+1):
        q = max(q, price_table[i] + cut_rod_dad(n-i, price_table))
    return q

def cut_rod(n, price_table):
    """
    dynamic programming: if n-i length has max profit calculated, it means, at length n, 
    you only consider n-i length and at i length, max(profit(n-1) + price(1), price(n))
    """
    dp = [0]*(n+1)
    for cut in range(1, n+1):
        for price_len, price in enumerate(price_table):
            if cut >= price_len:
                dp[cut] = max(dp[cut - price_len] + price, dp[cut])
    return dp[n]

def cut_rod_extended(n, price_table):
    """
    extend to show the combination of cutting length
    for example: when n = 4, the best cut is to cut into two equal lengths.
    """
    dp = [0]*(n + 1)
    solution_path = [0]*(n + 1)
    for cut in range(1, n + 1):
        for price_len, price in enumerate(price_table):
            if cut >= price_len and (dp[cut - price_len] + price > dp[cut]):
                dp[cut] = dp[cut - price_len] + price
                solution_path[cut] = price_len
    return dp[n], [solution_path[-1], n-solution_path[-1]]


if __name__ == "__main__":
    price_table = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30] #index is the length of a rod, with value is its price
    rod_length = 4 
    profit, best_cut = cut_rod_extended(rod_length, price_table)
    print(profit, best_cut)