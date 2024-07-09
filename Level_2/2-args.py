if __name__ == "__main__":
    import sys
    arguments = sys.argv
    arguments_number = len(arguments)
    if len(arguments) == 0:
        print(f"{arguments_number} arguments.")
    elif len(arguments) == 1:
        print(f"{arguments_number} argument:/n{arguments[0]}")
    else:
        print(f"{arguments_number} arguments:/n{arguments}")
        