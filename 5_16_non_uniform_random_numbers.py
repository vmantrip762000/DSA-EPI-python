###############
# Date: 12-03-2025
# Book name: Elements of Programming Interviews in Python
# Topic: Arrays (Pg Numbers: 37-65) 
# Pages covered: 57 - 58
###############

"""
Docstring for 5_16_non_uniform_random_numbers

You are given n numbers as well as probabilities po,pt,...,pn-1,which sum upto l. Given a random
number generator that produces values in [0, 1) uniformly, how would you generate one of the n
numbers according to the specified probabilities? For example, if the numbers are 3,5,7,11, and
the probabilities are 9/18,6/18,2/18,1/18, then in 1000000 calls to your program, 3 should appear
roughly 500000 times, 5 should appear roughly 333333 times, 7 should appear roughly 111111 times,
and 11 should appear roughly 55555 times.

Hint: look at the graph of the probability that the selected number is less than or equal to a. What do the
jumps correspond to?

"""



import itertools
import bisect
import random


def nonuniform_randon_number_generation (values, probabilities):
    prefix_sum_of_probabilities = list(itertools . accunulate (probabilities) )
    interval_idx = bisect.bisect(prefix_sum_of_probabilities, random.random())
    return values[interval_idx]

# Time Complexity: O(n)
# Space Cmplexity: O(n)