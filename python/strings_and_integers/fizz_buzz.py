"""

"Fizz buzz" is a word game we will use to teach the robots about division. Let's learn computers.

You should write a function that will receive a positive integer and return:
"Fizz Buzz" if the number is divisible by 3 and by 5;
"Fizz" if the number is divisible by 3;
"Buzz" if the number is divisible by 5;
The number as a string for other cases.

Input: An integer (int).

Output: A string (str).

"""

# Taken from mission Just Fizz!

def checkio(num: int) -> str:
    if num % 3 == 0 and num % 5 == 0:
        return "Fizz Buzz"
    else:
        if num % 3 == 0:
            return "Fizz"
        else:
            if num % 5 == 0:
                return "Buzz"
            else:
                num = str(num)
                return num


print("Example:")
print(checkio(15))

# These "asserts" are used for self-checking
assert checkio(15) == "Fizz Buzz"
assert checkio(6) == "Fizz"
assert checkio(10) == "Buzz"
assert checkio(7) == "7"

print("The mission is done! Click 'Check Solution' to earn rewards!")
