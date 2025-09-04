""""

You are given a string and two markers (the initial and final). You have to find a substring enclosed between these two markers. But there are a few important conditions:

The initial and final markers are always different.
If there is no initial marker, then the first character should be considered the beginning of a string.
If there is no final marker, then the last character should be considered the ending of a string.
If the initial and final markers are missing then simply return the whole string.
If the final marker comes before the initial marker, then return an empty string.
example

Input: Three arguments. All of them are strings. The second and third arguments are the initial and final markers.

Output: A string.

"""

def between_markers(text: str, begin: str, end: str) -> str:
    """
    returns substring between two given markers
    """

    first_ocurr_begin = text.find(begin)
    first_ocurr_end = text.find(end)

    if first_ocurr_begin == -1 and first_ocurr_end != -1:
        return text[:first_ocurr_end]
    if first_ocurr_begin != -1 and first_ocurr_end == -1:
        return text[first_ocurr_begin + len(begin):]
    if first_ocurr_begin == -1 and first_ocurr_end == -1:
        return text
    if first_ocurr_begin > first_ocurr_end: 
        return ""
    else:
        return text[first_ocurr_begin + len(begin):first_ocurr_end]



print("Example:")
print(between_markers("What is >apple<", ">", "<"))

assert between_markers("What is >apple<", ">", "<") == "apple"
assert (
    between_markers("<head><title>My new site</title></head>", "<title>", "</title>")
    == "My new site"
)
assert between_markers("No[/b] hi", "[b]", "[/b]") == "No"
assert between_markers("No [b]hi", "[b]", "[/b]") == "hi"
assert between_markers("No hi", "[b]", "[/b]") == "No hi"
assert between_markers("No <hi>", ">", "<") == ""

print("The mission is done! Click 'Check Solution' to earn rewards!")