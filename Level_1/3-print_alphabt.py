# print uppercase letters excluding q and e

for i in range(65, 91):
    if chr(i) != 'Q' and chr(i) != 'E':
        print(chr(i), end=' ')