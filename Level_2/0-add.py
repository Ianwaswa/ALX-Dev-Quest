if __name__ == "__main__":
    from add_0 import add, subtract, multiply, divide
    
    a = int(input("Enter first integer: "))
    b = int(input("Enter second integer: "))
    
    print(f"{a} + {b} = {add(a, b)}")
    print(f"{a} - {b} = {subtract(a, b)}")
    print(f"{a} * {b} = {multiply(a, b)}")
    print(f"{a} / {b} = {divide(a, b)}")
    