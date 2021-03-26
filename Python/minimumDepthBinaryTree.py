# You are given a binary tree and you are asked to write a function that finds its minimum depth. The minimum depth can be defined as the number of nodes along the shortest path from the root down to the nearest leaf node. As a reminder, a leaf node is a node with no children.

# Example:
# Given the binary tree [5,7,22,None,None,17,9],

#     5
#    / \
#   7  22
#     /  \
#    17   9
# your function should return its minimum depth = 2.

# [execution time limit] 4 seconds (py3)

# [input] tree.integer root

# [output] integer
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def minimumDepthBinaryTree(root):

    def leftNode(node):
        if node == None:
            return 0
        if node != None:
            return 1
        
    def rightNode(node):
        if node == None:
            return 0
        if node != None:
            return 1


    def branch(root):
        if root == None:
            return 0
        count = 0
        if root.left == None and root.right == None:
            count += 1
        if leftNode(root.left) == 1 and rightNode(root.right) == 1:
            count += 1
            lb = branch(root.left)
            rb = branch(root.right)
            if lb < rb:
                count += lb
            else: 
                count += rb
        if leftNode(root.left) == 1 and rightNode(root.right) == 0:
            count += 1
            lb = branch(root.left)
            count += lb
        if leftNode(root.left) == 0 and rightNode(root.right) == 1:
            count += 1
            rb = branch(root.right)
            count += rb
        return count
     
    value = branch(root)
    return value