# You are given the prices of a stock, in the form of an array of integers, prices. Let's say that prices[i] is the price of the stock on the ith day (0-based index). Assuming that you are allowed to buy and sell the stock only once, your task is to find the maximum possible profit (the difference between the buy and sell prices).

# Note: You can assume there are no fees associated with buying or selling the stock.

# Example

# For prices = [6, 3, 1, 2, 5, 4], the output should be buyAndSellStock(prices) = 4.

# It would be most profitable to buy the stock on day 2 and sell it on day 4. Thus, the maximum profit is prices[4] - prices[2] = 5 - 1 = 4.

# For prices = [8, 5, 3, 1], the output should be buyAndSellStock(prices) = 0.

# Since the value of the stock drops each day, there's no way to make a profit from selling it. Hence, the maximum profit is 0.

# For prices = [3, 100, 1, 97], the output should be buyAndSellStock(prices) = 97.

# It would be most profitable to buy the stock on day 0 and sell it on day 1. Thus, the maximum profit is prices[1] - prices[0] = 100 - 3 = 97.
def buyAndSellStock(prices):
    difference = 0
    drop = 0
    for i in range(len(prices)):
        for element in range(i, len(prices)):
            if prices[element] - prices[i] > 0:
                result = prices[element] - prices[i]
                if result > difference:
                    difference = result
    return difference
a = [6, 5, 3, 2, 1]

buyAndSellStock(a)