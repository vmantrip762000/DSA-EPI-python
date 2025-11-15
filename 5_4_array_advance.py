def can_reach_end(A):
    furthest_reached_so_far, max_end = 0, len(A)-1
    i=0
    steps = 0
    while i <= furthest_reached_so_far and furthest_reached_so_far <= max_end:

        if abs(furthest_reached_so_far - max(i + A[i], furthest_reached_so_far)) > 0:
            steps += 1
        furthest_reached_so_far = max(i + A[i], furthest_reached_so_far)        
        print(furthest_reached_so_far)
        i += 1

    reached_descision = furthest_reached_so_far >=  max_end 

    if reached_descision:
        return furthest_reached_so_far >=  max_end, steps
    return reached_descision

print(can_reach_end([3,3,7,0,2,0,1]))
print(can_reach_end([3,2,0,0,2,0,7]))
print(can_reach_end([2,4,1,1,0,2,3]))
