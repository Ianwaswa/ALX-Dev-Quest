decimal_number = int(input("Enter any whole number: "))
def decimal_to_octal(num):
    
    octal_value = ""
    
    while num > 0:
        remainder = num % 8
        octal_value = octal_value + str(remainder)
        num = num // 8
    return octal_value[::-1]

output = decimal_to_octal(decimal_number)

print("The octal equivalent of", decimal_number, "is:", output)
