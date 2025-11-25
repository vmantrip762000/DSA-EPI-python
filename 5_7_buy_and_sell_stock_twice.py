###############
# Date: 11-25-2025
# Book name: Elements of Programming Interviews in Python
# Topic: Arrays (Pg Numbers: 37-65) 
# Pages covered: 47 - 48
###############


"""
Docstring for 5_7_buy_and_sell_stock_twice

Write a program that computes the maximum profit that can be made by buying and selling a share
at most twice. The second buy must be made on another date after the first sale.
"""

def buy_and_sell_twice(A):
    max_total_profit, min_price_so_far = 0.0, float('inf')
    first_buy_sell_profits = [0] * len(A)

    # Forward phase
    for i, price in enumerate(A):
        min_price_so_far = min(price, min_price_so_far)
        max_total_profit = max(max_total_profit, A[i] - min_price_so_far)# For each day we calculate maximum profit UNTIL that day.
        first_buy_sell_profits[i] = max_total_profit # Maximum profit until that day is noted in the array
    
    # Backward phase
    max_price_so_far = float('-inf')
    for i, price in reversed(list(enumerate(A[1:], 1))):
        max_price_so_far = max(max_price_so_far, price)
        max_total_profit = max(max_total_profit, max_price_so_far - price + first_buy_sell_profits[i - 1])
        # Above, max_price_so_far - price is the second sell and buy respectively

    return max_total_profit

print(buy_and_sell_twice([12,11,13,9,12,8,14,13,15]))

# Time Complexity: O(n)
# Space complexity: O(n)
