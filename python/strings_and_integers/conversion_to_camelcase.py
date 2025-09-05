def to_camel_case(name: str) -> str:
    final_str = ""
    flag = False
    title_it = True
    
    for char in name:
        if flag == True:
            final_str += char.upper()
            flag = False
            continue
        if name.index(char) == 0 and title_it:
            final_str += char.upper()
            title_it = False
            continue
        elif char == "_":
            flag = True
            continue
        else: 
            final_str += char
    return final_str


print("Example:")
print(to_camel_case("my_function_name"))

# These "asserts" are used for self-checking
assert to_camel_case("my_function_name") == "MyFunctionName"
assert to_camel_case("i_phone") == "IPhone"

print("The mission is done! Click 'Check Solution' to earn rewards!")
