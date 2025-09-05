def from_camel_case(name: str) -> str:
    final_str = ""
    for char in name:
        if char == char.upper() and name.index(char) != 0:
            final_str += f'_{char.lower()}'
        else:
            final_str += char.lower()
    return final_str


print("Example:")
print(from_camel_case("MyFunctionName"))

# These "asserts" are used for self-checking
assert from_camel_case("MyFunctionName") == "my_function_name"
assert from_camel_case("IPhone") == "i_phone"

print("The mission is done! Click 'Check Solution' to earn rewards!")
