def replace_vowels(str):
    vowels = "AEIOUaeiou"
    result = ""
    for char in str:
        if char in vowels:
            result += "*"
        else:
            result += char
    return result
print(replace_vowels("OpenAI")) # *p*n**