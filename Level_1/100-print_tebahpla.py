for i in range(122, 97, -1):
    if (122 - i) % 2 != 0:
        print(chr(i - 32), end=" ")
    else:
        print(chr(i), end=" ")