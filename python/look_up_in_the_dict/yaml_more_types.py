# Taken from mission YAML. Simple Dict

def yaml(a: str) -> dict:

    text_dict = a.splitlines()
    final = {}

    for text in text_dict:
        _list = text.split(":")

        if len(_list) < 2:
            print(_list[0], _list[-1])
            continue
        
        if _list[-1].strip().isdigit():
            final[_list[0]] = int(_list[-1].strip())
            continue

        elif _list[-1].strip().startswith('"') and _list[-1].strip().endswith('"'):

            if '\\"' in _list[-1].strip().strip('"'):
                final[_list[0]] = _list[-1].strip().replace('\\', '')[1:-1]

            else:
                final[_list[0]] = _list[-1].strip().strip('"')

            continue

        elif _list[-1].strip().lower() == 'false':
            final[_list[0]] = False
            continue

        elif _list[-1].strip().lower() == 'true':
            final[_list[0]] = True
            continue

        elif _list[-1].strip().lower() in ('null', 'none') or _list[-1].strip() == '':
            final[_list[0]] = None
            continue
        
        final[_list[0]] = _list[-1].strip()

    return final


print("Example:")
print(yaml('name: "Bob Dylan"\nchildren: 6\ncoding:'))

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
