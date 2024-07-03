whole_number = int(input("Enter any whole number: "))
def number_to_octal(num):
    
    octal_num = ""
    
    while num > 0:
        remainder = num % 8
        octal_num = octal_num + str(remainder)
        num = num // 8
    return octal_num[::-1]

output = number_to_octal(whole_number)

print("The octal equivalent of", whole_number, "is:", output)