def islower(c):
    # Get the Unicode code point of the character
    code_point = ord(c)
    # Check if it is in the range of lowercase letters
    if 97 <= code_point <= 122:
        return True
    else:
        return False
print(islower('a'))