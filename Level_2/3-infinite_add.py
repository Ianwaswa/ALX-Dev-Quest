if __name__ == "__main__":
    
    import sys
    argv = sys.argv[1:]
    arg_count = len(argv)
    result = 0
    
    for i in range(1, arg_count):
        result += int(arg_count)
    
    print(f"Result: {result}")