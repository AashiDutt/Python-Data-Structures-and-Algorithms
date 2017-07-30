# FIFO -First In First Out

class Queue:
    
    def __init__(self):            #constructor
        
        self.queue=[]              # create 1D array
        
        
    def isEmpty(self):
        
        return self.queue==[]      #if empty return True else False
    
    
    
    def enqueue(self , data):      # adding data tothe queue
    
        self.queue.append(data)
        
        
        
    def dequeue(self):             # removing first item using FIFO
        
        data =self.queue[0]
        
        del self.queue[0]          #remove the reference
        
        return (data)
    
    
    def peek(self):
        
        return self.queue[0]
        
    def sizeQueue(self):
        
        return len(self.queue)
queue=Queue()

queue.enqueue(10)

queue.enqueue(20)

queue.enqueue(30)

print(queue.sizeQueue())

print(" Dequeue : ",queue.dequeue())

print(" Dequeue : ",queue.dequeue())


print(queue.sizeQueue())    
