def magic_calculation(a, b, c):
    if a < b:
        return c
    if c > b:
        return a + b
    return (a * b) - c
magic_calculation(12, 15, 10)