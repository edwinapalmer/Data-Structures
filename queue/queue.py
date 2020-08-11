"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
class Queue:
    def __init__(self):
        self.size = 8
        self.storage = 0
        self.queue = list()
        self.head = 0
        self.tail = 0
    
    def __len__(self):
        return self.tail - self.head

    def enqueue(self, value):
        if self.storage >= self.size:
            return ("full")
        self.queue.append(value)
        self.tail += 1
        return True

    def dequeue(self):
        if self.size <= 0:
            self.resetQueue()
            return None
        value = self.queue
        self.head+=1
        return value

    def resetQueue(self):
        self.tail = 0
        self.head = 0
        self.queue = list()



