
# Taken from mission YAML. Simple Dict
def yaml(a: str) -> dict:
    text_dict = a.splitlines()
    final = {}
    for text in text_dict:
        if text.strip().startswith("#"):
            text = text[: text.index("#"):-1]
        
        if text.startswith("-"):
            pass


        # _list = text.split(":")
        # if len(_list) < 2:
        #     print(_list[0], _list[-1])
        #     continue
        
        # if _list[-1].strip().isdigit():
        #     final[_list[0]] = int(_list[-1].strip())
        #     continue
        # elif _list[-1].strip().startswith('"') and _list[-1].strip().endswith('"'):
        #     if '\\"' in _list[-1].strip().strip('"'):
        #         final[_list[0]] = _list[-1].strip().replace('\\', '')[1:-1]
        #     else:
        #         final[_list[0]] = _list[-1].strip().strip('"')
        #     continue
        # elif _list[-1].strip().lower() == 'false':
        #     final[_list[0]] = False
        #     continue
        # elif _list[-1].strip().lower() == 'true':
        #     final[_list[0]] = True
        #     continue
        # elif _list[-1].strip().lower() in ('null', 'none') or _list[-1].strip() == '':
        #     final[_list[0]] = None
        #     continue
        
        # final[_list[0]] = _list[-1].strip()
    return final


print("Example:")
print(yaml('- write some\n- "Alex Chii"\n- 89'))

# These "asserts" are used for self-checking
assert yaml('- write some\n- "Alex Chii"\n- 89') == ["write some", "Alex Chii", 89]
assert yaml(
    '# comment\n- write some # after\n# one mor\n- "Alex Chii #sir "\n- 89 #bl'
) == ["write some", "Alex Chii #sir ", 89]
assert yaml("- 1\n- 2\n- 3\n\n- 4\n\n\n\n- 5") == [1, 2, 3, 4, 5]
assert yaml("-\n-\n-\n- 7") == [None, None, None, 7]

print("The mission is done! Click 'Check Solution' to earn rewards!")
