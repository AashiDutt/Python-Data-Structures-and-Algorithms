# Ternary search trees implementation

class Node(object):

    # constructer
    def __init__(self , character):
        self.character = character
        self.leftNode = None
        self.rightNode = None
        self.middleNode = None
        self.value = 0            #intialising value to 0

class TST(object):

    def __init__(self):
        self.rootNode = None

    #  Function to Insert a Node
    # We are using "0" as the index of the input string.
    # This helps to track that at which character of string the value is stored.

    def put(self,key,value):
        self.rootNode = self.putItem(self.rootNode, key,value, 0)   #0  index of given string key

    def putItem(self, node, key,value,index):

        c = key[index]    #character with a given key using index

        if node == None :
            node = Node(c)

        # if i/p character is smaller than previous then move to left else move right
        # If we go to left or right, it means we are still on same character and it is either smaller or greater than the
        # current character. Hence, index value remains the same.

        if c < node.character:
            node.leftNode = self.putItem(node.leftNode , key, value, index)

        elif c > node.character :
            node.rightNode = self.putItem(node.rightNode , key , value , index)

        elif index < len(key) :   # represents index of the last character
            node.middleNode = self.putItem(node.middleNode, key ,value , index+1)

        else:
            node.value = value
        return node


    def get(self , key):

        node =self.getItem(self.rootNode, key, 0)

        if node == None:
            return -1
       # return node.value

        # Function to get an item from the TST using Key
        def getItem(self, node, key, index):
            # If the node does not exists, return None
            if node == None:
                return None

        # Take the string character by character and traverse the tree.
        c = key[index]

        if c < node.character:
            return self.getItem(node.leftNode , key ,index)

        elif c > node.character:
            return self.getItem(node.rightNode , key , index)

        elif index < len(key) :
            return self.getItem(node.middleNode, key , index+1)
        else:
            return node

    if __name__ == "__main__":
        tst = TST()

        tst.put("äpple",100)
        tst.put("orange",200)

        print(tst.get("apple"))


# -------------------------- EOC ---------------------------------