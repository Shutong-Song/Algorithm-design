### coin change problem is similar like the knapsack problem (see knapsack.py)


# coin change with greedy algorithm
def coin_change_greedy(amount):
    """
    only some coin change problem can be solved by greedy algorithm, greedy algorithm requires safe choice
    each coin can be used infinite  times
    time complexity: O(n*log(n)) + O(amount) where n is the number of coins
    """
    coins = [10, 5, 1]
    mini = 0
    for coin in coins:
        while amount >= coin:
            amount -= coin
            mini += 1
    return mini


# coin change using Dynamic programming
def coin_change_dp(coins, amount):
    """
    repeated coin change with each coin in coins list can be used infinite of times
    input: a list of coins, total amount to be changed 
    ouput: the combination of coins that made the change
    time complexity: O(n*m) where n is number of coins, m is the amount value
    space complexity: O(m)
    """
    dp = [0] + [float("inf")]*amount
    change_comb = ["0"] + [""]*amount
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                change_comb[i] = str(change_comb[i - coin]) + " " + str(coin)
    return dp[amount], change_comb[amount]


def coin_change_nonrep(coins, amount):
    """
    this problem is similar with knapsack without repetition,
    except that knapsack is gurantteed has a maximum values return, but here is amount can not be reached by using
    coin in coins, we cannot make that change
    """
    pass


if __name__ == "__main__":
    coins = [186, 419, 83, 408]
    amount = 6249
    num_changes, change_detail = coin_change_dp(coins, amount)
    print("total number of changes made: ",num_changes)
    print("\n")
    print(change_detail)
