# creating heap with python built in libraray
#create heaps in o(n) time complexity

from heapq import heappop, heappush ,heapify

heap = []                       # create 1D array for heap
nums =[12,3,-2,6,4,8,9]        #1D arry for integers

for num in nums:
    heappush(heap, num)       #enter numbers in hep from integer array

while heap:
     print(heappop(heap))       #'heappop returns to root node everytime python iterates

heapify(nums)

print(nums)                # output of heapify ---> [-2, 3, 8, 6, 4, 12, 9]
