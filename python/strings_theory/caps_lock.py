"""

Joe Palooka has fat fingers, so he always hits the “Caps Lock” key whenever he actually intends to hit the key “a” by itself. (When Joe tries to type in some accented version of “a” that needs more keystrokes to conjure the accents, he is more careful in the presence of such sophisticated characters ([Shift] + [a]) and will press the keys correctly.) Compute and return the result of having Joe type in the given text. The “Caps Lock” key affects only the letter keys “a” and “z”, and has no effect on the other keys or characters. The “Caps Lock” key is assumed to be initially off.

For Joe's keyboard, Caps Lock always uppercases a letter. That means if Caps Lock is on, and Joe does Shift + b, 'B' (in upper case) gets printed.

Input: A string (str). The typed text.

Output: A string (str). The resulting text after being typed.

"""

def caps_lock(text: str) -> str:
    final_word = ""
    caps = False
    while text != "":
        index = text.find("a")
        if index != -1:
            final_word += text[:index].replace("a", "").upper() if caps else text[:index].replace("a", "")
            text = text[index+1:]
            caps = not caps
        else: 
            final_word += text.upper() if caps else text
            text = ""

    return final_word


print("Example:")
print(caps_lock("Why are you asking me that?"))
print(caps_lock("Always wanted to visit Zambia."))
print(caps_lock("Aloha from Hawaii"))

# These "asserts" are used for self-checking
assert caps_lock("Why are you asking me that?") == "Why RE YOU sking me thT?"
assert caps_lock("Always wanted to visit Zambia.") == "AlwYS Wnted to visit ZMBI."
assert caps_lock("Aloha from Hawaii") == "Aloh FROM HwII"

print("The mission is done! Click 'Check Solution' to earn rewards!")
