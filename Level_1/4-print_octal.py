whole_number = int(input("Enter any whole number: "))
def number_to_octal(num):
    
    octal_num = ""
    
    while num > 0:
        remainder = num % 8
        octal_num = str(remainder) + octal_num
        num = num // 8
    return octal_num

output = number_to_octal(whole_number)

print("The octal equivalent of", whole_number, "is:", output)