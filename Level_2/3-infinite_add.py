if __name__ == "__main__":
    
    import sys
    argv = sys.argv[1:]
    sum_total = sum(int(arg) for arg in argv)
    print(f"{sum_total}")