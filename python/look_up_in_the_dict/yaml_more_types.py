# Taken from mission YAML. Simple Dict

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
print(yaml("name: Alex\nage: 12"))
print(yaml("name: Alex Fox\nage: 12\n\nclass: 12b"))

# These "asserts" are used for self-checking
assert yaml("name: Alex\nage: 12") == {"name": "Alex", "age": 12}
assert yaml("name: Alex Fox\nage: 12\n\nclass: 12b") == {
    "name": "Alex Fox",
    "age": 12,
    "class": "12b",
}
assert yaml('name: "Alex Fox"\nage: 12\n\nclass: 12b') == {
    "name": "Alex Fox",
    "age": 12,
    "class": "12b",
}
assert yaml('name: "Alex \\"Fox\\""\nage: 12\n\nclass: 12b') == {
    "name": 'Alex "Fox"',
    "age": 12,
    "class": "12b",
}
assert yaml('name: "Bob Dylan"\nchildren: 6\nalive: false') == {
    "name": "Bob Dylan",
    "children": 6,
    "alive": False,
}
assert yaml('name: "Bob Dylan"\nchildren: 6\ncoding:') == {
    "name": "Bob Dylan",
    "children": 6,
    "coding": None,
}
assert yaml('name: "Bob Dylan"\nchildren: 6\ncoding: null') == {
    "name": "Bob Dylan",
    "children": 6,
    "coding": None,
}
assert yaml('name: "Bob Dylan"\nchildren: 6\ncoding: "null" ') == {
    "name": "Bob Dylan",
    "children": 6,
    "coding": "null",
}

print("The mission is done! Click 'Check Solution' to earn rewards!")
