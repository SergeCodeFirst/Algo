# # class TreeNode:
# #     def __init__(self, value):
# #         self.left = None
# #         self.right = None
# #         self.value = value

# #     def insert(self, value):
# #         if value < self.value:
# #             if self.left != None:
# #                 self.left.insert(value)
# #             else:
# #                 self.left = TreeNode(value)
# #         else:
# #             if self.right != None:
# #                 self.right.insert(value)
# #             else:
# #                 self.right = TreeNode(value)

# #     def inorder_traversal(self):
# #         if self.left:
# #             self.left.inorder_traversal()
# #         print(self.value)

# #         if self.right:
# #             self.right.inorder_traversal()

# #     def preorder_traversal(self):
# #         print(self.value)
# #         if self.left:
# #             self.left.preorder_traversal()

# #         if self.right:
# #             self.right.preorder_traversal()

# #     def postorder_traversal(self):
# #         if self.left:
# #             self.left.postorder_traversal()

# #         if self.right:
# #             self.right.postorder_traversal()
# #         print(self.value)

# #     def find(self, value):
# #         if self.value == value:
# #             return True
        
# #         if value < self.value:
# #             if self.left == None:
# #                 return False
# #             else:
# #                 return self.left.find(value) # why should we retun this and not just call it
        
# #         if value > self.value:
# #             if self.right == None:
# #                 return False
# #             else:
# #                 return self.right.find(value) # why should we retun this and not just call it


# # newTree = TreeNode(10)

# # newTree.insert(5)
# # newTree.insert(4)
# # newTree.insert(2)
# # newTree.insert(1)
# # newTree.insert(3)
# # newTree.insert(22)
# # newTree.insert(11)
# # newTree.insert(12)

# # # newTree.preorder_traversal()

# # print(newTree.find(12))




# # =============================
# #           VERSION 2
# # =============================


# class Node:
#     def __init__(self, value=None):
#         self.value = value
#         self.left = None
#         self.right = None

# class BinaryTree:
#     def __init__(self, root=None):
#         self.root = root

#     def add(self, value):
#         new_node = Node(value)
        


#         if value < self.root.value:
#             if self.root.left:
#                 self._insert(self.root.left, value)
#             self.root.left = new_node
#         else:
#             if cur_node.right:
#                 cur_node.right.add(value)
#             cur_node.right = new_node

#     def _insert(self, node, value):



#     # def display(self):
#     #     cur = self.root
#     #     while cur.left:
#     #         self.root.left.display()
#     #         cur = cur.left
#     #     print(self.root.value)

#     #     if self.root.right:
#     #         self.root.right.display()


# root_node = Node(5)


# new_Tree = BinaryTree(root_node)
# new_Tree.add(6)
# new_Tree.add(2)
# new_Tree.add(10)


# # new_Tree.display()
