# stacks

# operations in stacks

class Stack:                      # form a class

    def __init__(self):          #constructor
        self.stack=[]             # create stacked named 1D array
        
        
        
    # define method to check wheather given stack is empty or not
    def isEmpty(self):            
        return self.stack==[]     # if it is empty array it will return true (bool)
        
        
    # push operation  
    # O(1) time complexity
    def push(self , data):
        self.stack.append(data)   # append item in 1D array
      
      
      #pop operation  
      # O(1) time complexity
      # use LIFO structure(Last In First Out)
      
    def pop(self):                # pops value and removes the item 
        data= self.stack[-1]      # get last item from stack
        del self.stack[-1]        # delete the reference
        return (data)
        
    #peek  operation
    
    def peek(self):               # gives value of last item without removing it (abstract data type)
        return self.stack[-1]          # returns last value entered without need of removing it
        
    # finding size of array
    #returns how many items the stack contains
    
    def sizeStack(self):
        return len(self.stack)   
        
        
stack =Stack()

stack.push(1)

stack.push(2)

stack.push(3)

print(stack. sizeStack())

print("popped  ",stack.pop())

print("popped  ",stack.pop())

print(stack. sizeStack())

print("peek  ", stack.peek())

print(stack. sizeStack())
print(stack. sizeStack())
