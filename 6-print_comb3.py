for i in range(1, 10):
    for y in range(i + 1, 10):
        if (not(i == 8 and y == 9)):
            print(f"{i}{y}", end=", ")
        else:
            print(f"{i}{y}")