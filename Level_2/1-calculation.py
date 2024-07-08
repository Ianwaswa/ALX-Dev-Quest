if __name__ == "__main__":
    import calculator_1
    a = 10
    b = 5
    
    sum = calculator_1.add(a, b)
    difference = calculator_1.sub(a, b)
    product = calculator_1.mul(a, b)
    quotient = calculator_1.div(a, b)
    
print("{} + {} = {}".format(a, b, sum))
print("{} - {} = {}".format(a, b, difference))
print("{} * {} = {}".format(a, b, product))
print("{} / {} = {}".format(a, b, quotient))