"""
Write a program which takes as input an array of digits encoding a nonnegative decimal integer
D and updates the array to represent the integer D + 1. For example, if the input is (7,2,9) then
you should update the array to (1,3,0). Your algorithm should work even if it is implemented in a
language that has finite-precision arithmetic.
Hint: Experiment with concrete examples.

"""


def plus_one(A) :
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i - 1] += 1
    if A[0] == 10:
        # There is a carry-out, so we need one more digit to store the result
        # A slick way to do this is to append a 0 at the end of the array,
        # and update the first entry to 1.
        A[0] = 1
        A.append (0)
    return A

#print(plus_one([9]))


"""
Write a program that takes two arrays representing integers, and retuns an integer representing
their product. For example, since 193707721.x -761838257287 = -147573952589676412927, if
the inputs are (1,9,3,7,0,7,7,2, 1) and <-7,6,L,8,3,8,2,5,7,2,8,7>, your function should return
(-1, 4,7, 5,7,3, 9, 5, 2, 5,8,9, 6,7, 6, 4, 1., 2,9,2,7>.
Hint: Use arrays to simulate the grade-school multiplication algorithm.

"""


def multiply(num1, num2):
    sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1
    num1[0] , num2[0] = abs (num1[0]), abs(num2[0])
    result = [0] * (len(num1) + len(num2))
    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))) :
            result[i + j + 1] += num1[i] * num2[j]
            result[i + j] += result[i + j + 1] // 10
            result[i+j+1]%=10
    # Remove the leading zeroes,
    result = result[next((i for i, x in enumerate(result)
    if x != 0), len(result)):] or [0]
    return [sign * result[0]] + result[1:]

#print(multiply([1,2,3], [4,5,6]))