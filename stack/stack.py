"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
class Stack:
    def __init__(self):
        self.size = 9
        self.storage = 0
        self.stack = list()

    def __len__(self):
        return len(self.stack)

    def push(self, value):
        if self.storage>=self.size:
            return ("full!")
        self.stack.append(value)
        self.storage += 1
        return True

    def pop(self):
       if self.storage<=0:
           return None
       item = self.stack.pop()
       self.storage -= 1
       return item
    



# The storage space on arrays need to be resized for elements stored in them whenever they are added or removed.
# The storage space is allocated more than required, so that not every push or pop requires resizing and you 
# get an amortized O(1) time complexity for these operations.
# This makes their performance less consistent than the stable O(1) inserts and deletes provided by a 
# linked list-based implementation. On the other hand, lists provide fast O(1) time random access to elements on the 
# stack which is an added benefit.



