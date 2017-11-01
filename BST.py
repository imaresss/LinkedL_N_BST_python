class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None

class BST:
    root= Node(-1)
    
    def make(data):
        newNode = Node(data)
        if(BST.root.data==-1):
            BST.root= newNode
         else:
            BST.after_root(BST.root, data, newNode)

    def after_root(root,data,newNode):

        if(data<root.data and root.left==None):
            root.left=newNode
        elif(data>root.data and root.right==None):
            root.right=newNode
        elif(data<root.data):
            BST.after_root(root.left,data, newNode)
        elif(data>root.data):
            BST.after_root(root.right,data, newNode)

    def inorder(root):
        if(root!=None):
            BST.inorder(root.left)
            print(root.data)
            BST.inorder(root.right)
            
class Main:

    BST.make(10)
    BST.make(4)
    BST.make(15)
    BST.make(2)
    BST.make(12)
    BST.inorder(BST.root)

    
