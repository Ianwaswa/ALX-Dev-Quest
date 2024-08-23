import sys

for line in sys.stdin:
    if 'q' == line.strip():
        break
    print(f'Input: {line}')
    
print('Exiting...')