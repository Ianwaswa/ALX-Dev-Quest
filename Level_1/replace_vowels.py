def replace_vowels(str):
    vowels = "AEIOUaeiou"
    result = ""
    for vowel in vowels:
        if vowel in vowels:
            result += "*"
        else:
            result += vowel
    print(result)
print(replace_vowels("OpenAI")) # *p*n**