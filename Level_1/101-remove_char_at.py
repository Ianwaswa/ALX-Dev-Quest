def remove_char_at(str, n):
    if n < 0 and n >= len(str):
        return str
    return str[:n] + str[n+1:]
print(remove_char_at("OpenAI", 5)) # OpenA