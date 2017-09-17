"""
In this challenge, you must first implement a queue using two stacks.
Then process queries, where each query is one of the following 3 types:

    1 x: Enqueue element into the end of the queue.
    2: Dequeue the element at the front of the queue.
    3: Print the element at the front of the queue.
"""

class MyQueue(object):
    def __init__(self):
        self.stack = []
    
    def peek(self):
        return(self.stack[0])
        
        
    def pop(self):
        self.stack.pop(0)
        
        
    def put(self, value):
        self.stack.append(value)

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
        
