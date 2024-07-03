
def islower(c):
    code_point = ord(c)
    if  97 <= code_point <= 122:
        return True
    else:
        return False
print(islower('a'))