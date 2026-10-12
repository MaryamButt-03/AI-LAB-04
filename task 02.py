# implement queue using python
queue = []

# Enqueue
queue.append(10)
queue.append(20)
queue.append(30)

print("Queue:", queue)

# Dequeue
print("Removed:", queue.pop(0))

print("Queue after dequeue:", queue)

# Front
print("Front element:", queue[0])

# Check empty
if len(queue) == 0:
    print("Queue is empty")
else:
    print("Queue is not empty")