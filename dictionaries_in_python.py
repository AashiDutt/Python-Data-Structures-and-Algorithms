#Dictionaries in python

#creating a dictionary

dict = {'Joe':14, 'Adam':26, 'Émily':56}

print(dict['Joe'])  #O(1) time complexity

# replacing or editing the dictionary

#dict['Joe'] = 15
print(dict['Joe'])

# clearing all memories from the dictionary
dict.clear()

#deleting the dictionary
del dict

#printing all items of dictionary
print(dict.items())


#returning all keys
print(dict.keys())


#print out all values
print( dict.values())

#disadvantages -- > this data structure do not follow any ordering

#advantages --> insertion and retrival takes O(1) complexity
#           --> for arrays takes O(N) time complexity
# for balanced binary search tree takes O(logN) complexity
