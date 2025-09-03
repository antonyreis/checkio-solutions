"""

Identify whether a given integer is positive, negative, or zero and return a respective string: "positive", "negative" or "zero".

Input: Integer (int).

Output: String (str).

How it's used: understanding the sign of a number can be useful in financial software, scientific simulations, and many algorithms to determine subsequent logic.

Precondition:

num ∈ Z.
"""

def determine_sign(num):
    if num < 0:
        result = "negative"
    elif num == 0:
        result = "zero"
    else:
        result = "positive"
        
    return result


print("Example:")
print(determine_sign(11))

# These "asserts" are used for self-checking
assert determine_sign(5) == "positive"
assert determine_sign(0) == "zero"
assert determine_sign(-10) == "negative"
assert determine_sign(1) == "positive"
assert determine_sign(-1) == "negative"
assert determine_sign(999) == "positive"
assert determine_sign(-1000) == "negative"
assert determine_sign(123456789) == "positive"
assert determine_sign(-987654321) == "negative"
assert determine_sign(2) == "positive"

print("The mission is done! Click 'Check Solution' to earn rewards!")
