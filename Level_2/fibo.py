import sys

n = len(sys.argv) - 1
print("Total arguments passed:", n)
print("\nName of the script:", sys.argv[0])
print("\nArguments passed:", end=" ")

for i in range(1, n):
    print(sys.argv[i], end=" ")
Sum = 0
for i in range(1, n):
    Sum += int(sys.argv[i])

print("\n\nResult:", Sum)