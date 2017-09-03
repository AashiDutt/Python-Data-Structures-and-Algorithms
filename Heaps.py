# Creating Heap with python built in libraray.
# O(N) Time Complexity

from heapq import heappop, heappush ,heapify

# Create a 1D array for heap
heap = [] 

# 1D Input Array [Integers]
nums =[12,3,-2,6,4,8,9]        


for num in nums:
    heappush(heap, num)       # enter numbers in heap from integer array

    
while heap:
     print(heappop(heap))       # heappop returns to root node everytime python iterates

heapify(nums)

# output of heapify ---> [-2, 3, 8, 6, 4, 12, 9]
print(nums)                
# ------------------------- EOC --------------------------#
