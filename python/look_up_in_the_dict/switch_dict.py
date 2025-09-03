def switch_dict(data: dict[str, str]) -> dict[str, str]:
    final_dict = {}
    
    for key, value in data.items():
        if value not in final_dict:
            final_dict[value] = set()
            
        final_dict[value].add(key)
    return final_dict


print("Example:")
print(switch_dict({"rouses": "red", "car": "red", "sky": "blue"}))

# These "asserts" are used for self-checking
assert switch_dict({"rouses": "red", "car": "red", "sky": "blue"}) == {
    "red": {"car", "rouses"},
    "blue": {"sky"},
}
assert switch_dict({"1": "one", "2": "two", "3": "one", "4": "two"}) == {
    "one": {"1", "3"},
    "two": {"2", "4"},
}
assert switch_dict({"a": "b", "b": "c", "c": "a"}) == {
    "b": {"a"},
    "c": {"b"},
    "a": {"c"},
}

print("The mission is done! Click 'Check Solution' to earn rewards!")
