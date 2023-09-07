class TreeNode:
    def __init__(self, data=None, parent=None):
        self.data = data
        self.children = []
        self.parent = parent

    def add_child(self, child):
        child.parent = self
        self.children.append(child)
        return self
    

    def display_tree(self):
        for node in self.children:
            # print(f"parent:{self.data} -> {node.data}")
            spaces ="|__" * self.get_level()
            myStr = spaces + node.data
            print(myStr)
            node.display_tree()

    def get_level(self):
        count = 0
        p = self 
        while p.parent:
            count += 1
            p = self.parent

        return count




# ====================
#   HELPER FUNCTIONS
# ====================
def build_product_tree():
    rootNode = TreeNode("Electronic")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Dell"))
    laptop.add_child(TreeNode("Surface"))

    cellPhone = TreeNode("cellPhone")
    cellPhone.add_child(TreeNode("Iphone"))
    cellPhone.add_child(TreeNode("Google Pixel"))
    cellPhone.add_child(TreeNode("Vivo"))

    tv = TreeNode("tv")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    rootNode.add_child(laptop)
    rootNode.add_child(cellPhone)
    rootNode.add_child(tv)
    return rootNode 

myTree = build_product_tree()
myTree.display_tree()



# rootNode = TreeNode("Electronic")
# laptop = TreeNode("Laptop")
# laptop.add_child(TreeNode("Mac"))
# rootNode.add_child(laptop)
# print(laptop.get_level())
