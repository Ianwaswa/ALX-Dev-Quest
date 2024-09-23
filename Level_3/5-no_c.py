from collections import deque
stack = deque([1, 2, 3, 4])
stack.append(7)
stack.append(9)
stack.popleft()
print(stack)