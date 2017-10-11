from collections import deque
queue = deque(["Erick", "Jonh", "Michael"])
print queue
queue.append("Terry")
queue.append("Graham")
queue.popleft()
queue.popleft()

print (queue)