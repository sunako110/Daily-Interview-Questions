# 04 - Apr - 2020

# Maximum Profit From Stocks

# You are given an array. Each element represents the price of a stock on that particular day.
# Calculate and return the maximum profit you can make from buying and selling that stock only once.
#
# For example: [9, 11, 8, 5, 7, 10]
#
# Here, the optimal trade is to buy when the price is 5, and sell when it is 10,
# so the return value should be 5 (profit = 10 - 5 = 5).

def buy_and_sell(arr):
    # Fill this in.
    if len(arr) < 2:
        return

    i = 0
    max = 0
    while i < len(arr) - 1:

        while (i < len(arr) -1) and (arr[i+1] < arr[i]):
            i += 1
        if i == len(arr) - 1:
            return

        buy = arr[i]
        i += 1

        while (i < len(arr)) and (arr[i-1] <= arr[i]):
            i += 1
        sell = arr[i-1]

        if sell - buy > max:
            max = sell - buy
    return max

print(buy_and_sell([9, 11, 8, 5, 7, 10]))
# 5