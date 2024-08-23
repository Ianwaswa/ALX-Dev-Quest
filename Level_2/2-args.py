import sys

def main():
    argv = sys.argv
    arg_count = len(argv) - 1
    
    if arg_count == 0:
        print("No arguments provided.")
    elif arg_count == 1:
        print(f"One argument provided: {argv[1]}")
    else:
        print(f"{arg_count} arguments provided:")
    
    for i in range(1, len(argv)):
        print(f"{i}: {argv[i]}")

if __name__ == "__main__":
    main()