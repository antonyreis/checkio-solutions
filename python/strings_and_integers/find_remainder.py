"""
Input: Two integers (int): dividend (the number to be divided) and divisor (the number by which division is going to be performed).

Output: Integer (int).

Examples:

1
assert find_remainder(10, 3) == 1
2
assert find_remainder(14, 4) == 2
3
assert find_remainder(27, 4) == 3
4
assert find_remainder(10, 5) == 0
How it's used: remainder calculations are common in algorithms, especially in modular arithmetic which is frequently used in cryptography and computer graphics.
"""

def find_remainder(dividend, divisor):
    remainder = dividend%divisor
    return remainder


print("Example:")
print(find_remainder(3, 2))

# These "asserts" are used for self-checking
assert find_remainder(10, 3) == 1
assert find_remainder(14, 4) == 2
assert find_remainder(27, 4) == 3
assert find_remainder(10, 5) == 0
assert find_remainder(10, 1) == 0
assert find_remainder(5, 7) == 5
assert find_remainder(7, 5) == 2

print("The mission is done! Click 'Check Solution' to earn rewards!")
