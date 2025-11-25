###############
# Date: 11-21-2025
# Book name: Elements of Programming Interviews in Python
# Topic: Arrays (Pg Numbers: 37-65) 
# Pages covered: 46 - 47
###############



"""
Write a program that takes an array denoting the daily stock price, and returns the maximum profit
that could be made by buying and then selling one share of that stock. There is no need to buy if
no profit is possible.

Ex: [310,370,275,275,260,260,260,230,230,230]

"""

def buy_and_sell_stock(A):
    min_so_far, max_diff = float('inf'), 0.0
    #maximum diff = current_price - minimum_value_seen_so_far
    for i in range(len(A)):
        max_profit_today = A[i] - min_so_far
        max_diff = max(max_profit_today, max_diff)
        min_so_far = min(min_so_far, A[i])
    return max_diff


print(buy_and_sell_stock([310,370,275,275,260,260,260,230,230,230]))

# Space Complexity: O(1)
# Time Compleixity: O(n)



