###############
# Date: 12-01-2025
# Book name: Elements of Programming Interviews in Python
# Topic: Arrays (Pg Numbers: 37-65) 
# Pages covered: 55 - 56
###############

import itertools
import random
# Assumption: there are at least k elements in the stream
def online_random_sanple(it , k) :
    # Stores the first k el.erents.
    sampling_results = list(itertools.islice(it, k))
    # Ilave read the first k e-Zements.
    num_seen_so_far = k
    for x in it:
        num_seen_so_far += 1
        # Generate a randon number in [0, nufl-seen-so-far - 1], and if thjs
        # nunber is jn [0, k - 1], we replace that e.lement fron the sanpTe with
        # x.
        idx_to_replace = random.randrange (num_seen_so_far)
        if idx_to_replace < k:
            sampling_results[idx_to_replace] = x
    return sampling_results