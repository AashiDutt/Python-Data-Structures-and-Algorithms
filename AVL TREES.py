#AVL TREES for balanced consturction and o(logN) time complexity

class Node(object):
    
    def __init__(self,data):    #constructor
        self.data=data;         #entering data
        self.height=0;          #height of node
        self.leftChild=None;
        self.rightChild=None;

        
class AVL(object):
    
    def __init__(self):
        
        self.root=None;
        
    def insert(self , data):
        
        self.root = self.insertNode(data, self.root);
    def insertNode (self, data, node):
        
        if not node:
            return Node(data);
        
        if data< node.data:
            node.leftCild = self.insertNode(data , node.leftChild);
        else:
            node.rightChild = self.insertNode(data, node.rightChild);
            
        node.height = max(self.calaHeight(node.leftChild),self.calcHeoght(node.rightChild) )+1;
        return self.settleVoilation(data , node);
        
#calculate height of each node
#for leaf node return -1
        
    def calcHeight(self, node): 

        if not node:
            return -1;

#if returns value >1 means left heavy tree --> Right rotation
#if returns <-1 means right heavy tree --> Left rotation
        
    def calcBalance(self , node):

        if node node:
            return 0;
        return self.calcHeight(node.leftChild) - self.calcHeight(node.rightChild);

# rotating right
    def rotateRight(self ,node):
        
        print("Rotating to right on node ", node.data);

        tempLeftChild=node.leftChild;
        t=tempLeftChild.rightChild;

        tempLeftChild.rightChild= node; 
        node.leftChild =t;
        
#update reference of height after rotaion

        node.height= max(self.calcHeight(node.leftChild) , (self.calcHeight(node.rightChild)) +1;
        tempLeftChild.height= max(self.calcHeight(tempLeftChild.leftChild) , (self.calcHeight(tempLeftChild.rightChild)) +1;
        return tempLeftChild;


# rotating left
    def rotateLeft(self ,node):
        
        print("Rotating to left on node ", node.data);

        tempRightChild=node.rightChild;
        t=tempRightChild.leftChild;

        tempRighttChild.leftChild= node; 
        node.rightChild =t;
        
#update reference of height after rotaion

        node.height= max(self.calcHeight(node.leftChild) , (self.calcHeight(node.rightChild)) +1;
        tempRightChild.height= max(self.calcHeight(tempRightChild.leftChild) , (self.calcHeight(tempRightChild.rightChild)) +1;
        return tempRightChild;
                                  
