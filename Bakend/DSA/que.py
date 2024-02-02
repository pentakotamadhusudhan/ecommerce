from collections import deque

que= deque()
que.append("madhu1")
que.append("madhu2")
que.append("madhu3")
que.append("madhu4")

print(que.rotate())
# print(que.popleft())
print(que)

# # method two 
# que= []
# que.append("madhu1")
# que.append("madhu2")
# que.append("madhu3")
# que.append("madhu4")

# print(que)
# print(que.pop(0))
# print(que)

# method 3

# from queue import Queue
# q = Queue(maxsize = 3)
# print(q.qsize()) 
# q.put('a')
# q.put('b')
# q.put('c')
# print("\nFull: ", q.full()) 
# print("\nElements dequeued from the queue")
# print(q.get())
# print(q.get())
# print(q.get())
# print("\nEmpty: ", q.empty())
# q.put(1)
# q.put(1)
# q.put(1)
# print("\nEmpty: ", q.empty()) 
# print("Full: ", q.full())
