import logging
import time
from time import sleep

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -%(lineno)s - %(message)s')    
#Implement Stack and queue python
class myStack:
     def __init__(self):
         self.container = []  
         
     def isEmpty(self):
         return len(self.container) == 0  

     def push(self, item):
         self.container.append(item)  
         
     def pop(self):
         return self.container.pop() 
         
     def size(self):
         return len(self.container) 
     
     def get(self):
        return self.container
#############    
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    
    def get(self):
        return self.items
#################         
if __name__ == "__main__":
    stack = myStack()
    stack.push(1)
    stack.push(2) 
    stack.push(3)
    logging.info(f"Stack_list: {stack.get()}")#Output: [1, 2, 3]
    logging.info(f"Stack_list: {stack.pop()}")  # Output: 3
    logging.info(f"Stack_Size: {stack.size()}") # Output: 2
    logging.info(f"Check if stacksize is empty: {stack.isEmpty()}") # Output: False     
    sleep(2)
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    logging.info(f"Queue details: {queue.get()}") #Output: [3, 2, 1]
    logging.info(f"Dequeue from : {queue.dequeue()}")  # Output: 1
    logging.info(f"Queue size: {queue.size()}") # Output: 2 
    logging.info(f"Check if queue is empty: {queue.isEmpty()}") # Output: False  