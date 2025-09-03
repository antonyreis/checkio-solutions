# Taken from mission All Upper I

def is_all_upper(text) -> bool:
    if text and not text.isspace() and not text.isnumeric() and not text.strip(" ").isdigit():
        return text.upper() == text
    else:
        return False

print("Example:")
print(is_all_upper("ALL UPPER"))

# These "asserts" are used for self-checking
assert is_all_upper("ALL UPPER") == True
assert is_all_upper("all lower") == False
assert is_all_upper("mixed UPPER and lower") == False
assert is_all_upper("") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
