def yaml(a: str) -> dict:
    text_dict = a.splitlines()
    final = {}
    for text in text_dict:
        _list = text.split(":")
        if len(_list) < 2:
            continue
        
        final[_list[0]] = int(_list[-1].strip()) if _list[-1].strip().isdigit() else _list[-1].strip()
    return final


print("Example:")
print(
    yaml(
        """name: Alex
age: 12"""
    )
)

print(yaml("name: Alex Fox\nage: 12\n\nclass: 12b"))

# These "asserts" are used for self-checking
assert yaml("name: Alex\nage: 12") == {"name": "Alex", "age": 12}
assert yaml("name: Alex Fox\nage: 12\n\nclass: 12b") == {
    "age": 12,
    "name": "Alex Fox",
    "class": "12b",
}

print("The mission is done! Click 'Check Solution' to earn rewards!")
