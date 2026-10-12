# implement stack using python
stack = []

# Push
stack.append(11)
stack.append(22)
stack.append(33)

print("Stack:", stack)

# Pop
print("Popped:", stack.pop())

print("Stack after pop:", stack)

# Peek
print("Top element:", stack[-1])

# Check empty
if len(stack) == 0:
    print("Stack is empty")
else:
    print("Stack is not empty")
