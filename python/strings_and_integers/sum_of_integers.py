"""
Calculate sum of integers from 1 to given N (including).

Input: Integer (int).

Output: Integer (int).

How it's used: this function can be used in a variety of mathematical and algorithmic contexts, such as in calculating the nth triangular number, determining the cost for certain operations in algorithms, etc.

Precondition:

1 ≤ N ≤ 900.
"""

def sum_upto_n(N):
    result = 0
    for i in range(1,N+1):
        result += i
    return result


print("Example:")
print(sum_upto_n(11))

# These "asserts" are used for self-checking
assert sum_upto_n(1) == 1
assert sum_upto_n(2) == 3
assert sum_upto_n(3) == 6
assert sum_upto_n(4) == 10
assert sum_upto_n(5) == 15
assert sum_upto_n(10) == 55
assert sum_upto_n(20) == 210
assert sum_upto_n(100) == 5050
assert sum_upto_n(200) == 20100
assert sum_upto_n(500) == 125250

print("The mission is done! Click 'Check Solution' to earn rewards!")
