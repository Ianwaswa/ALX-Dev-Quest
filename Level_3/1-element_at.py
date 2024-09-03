def element_at(marks, idx):
    marks = [100, 112, 128, 114, 65]
    idx = int(input("Enter an index to check your marks: "))
    
    if idx < 0:
        return "Error: Index should be a non-negative integer."
    elif idx >= len(marks):
        return "Error: Index out of range."
    else:
        print("Your marks at index", idx, "is", marks[idx])

element_at(marks = '', idx = '')
    