class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):
        if value < self.value:
            if self.left != None:
                self.left.insert(value)
            else:
                self.left = TreeNode(value)
        else:
            if self.right != None:
                self.right.insert(value)
            else:
                self.right = TreeNode(value)

    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.value)

        if self.right:
            self.right.inorder_traversal()

    def preorder_traversal(self):
        print(self.value)
        if self.left:
            self.left.preorder_traversal()

        if self.right:
            self.right.preorder_traversal()

    def postorder_traversal(self):
        if self.left:
            self.left.postorder_traversal()

        if self.right:
            self.right.postorder_traversal()
        print(self.value)

    def find(self, value):
        if self.value == value:
            return True
        
        if value < self.value:
            if self.left == None:
                return False
            else:
                return self.left.find(value) # why should we retun this and not just call it
        
        if value > self.value:
            if self.right == None:
                return False
            else:
                return self.right.find(value) # why should we retun this and not just call it


newTree = TreeNode(10)

newTree.insert(5)
newTree.insert(4)
newTree.insert(2)
newTree.insert(1)
newTree.insert(3)
newTree.insert(22)
newTree.insert(11)
newTree.insert(12)

# newTree.preorder_traversal()

print(newTree.find(12))

