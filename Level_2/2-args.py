if __name__ == "__main__":
    
    import sys
    argv = sys.argv[1:]
    arguments = sys.argv
    arguments_number = len(arguments)
    
    if len(arguments) == 0:
        print(f"{arguments_number} arguments.")
    elif len(arguments) == 1:
        print(f"{arguments_number} argument:")
        print(f"{arguments[0]}")
    elif len(arguments) > 1:
        print(f"{arguments_number} arguments:")
        for i in range(1, arguments_number):
            print(f"{arguments[i]}")
        