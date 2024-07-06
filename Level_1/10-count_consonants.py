def count_consonants(str):
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    count = 0
    for char in str:
        if char in consonants:
            count += 1
        elif char == " ":
            continue
    return count
print(count_consonants("OpenAI")) # 3