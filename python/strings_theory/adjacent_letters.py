def adjacent_letters(line: str) -> str:

    original_list = list(line)
    final_word = []

    for char in original_list:
        if len(final_word) == 0:
            final_word.append(char)
            continue

        elif final_word[-1] == char:
            final_word.pop()
            continue

        final_word.append(char)
        
    return ''.join(final_word)


print("Example:")
print(adjacent_letters("abbaca"))

# These "asserts" are used for self-checking
assert adjacent_letters("adjacent_letters") == "adjacent_lrs"
assert adjacent_letters("") == ""
assert adjacent_letters("aaa") == "a"
assert adjacent_letters("ABBA") == ""

print("The mission is done! Click 'Check Solution' to earn rewards!")
