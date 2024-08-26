import sys

def main():
    argv = sys.argv[1:]
    result = 0
    
    for arg in argv:
        result += int(arg)
    
    print(f"Result: {result}")

if __name__ == "__main__":
    main()