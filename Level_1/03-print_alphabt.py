# Print uppercase alphabet except for 'K' and 'F' but here we using a different approach

def main():
    for letters in 'ABCDEFGHKLMNOPQRSTUVWXYZ':
        if letters.isalpha() and letters.upper() != 'K' and letters.upper() != 'F':
            print(letters.upper(), end=' ')
main()