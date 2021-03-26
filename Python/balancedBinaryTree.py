# You are given a binary tree and you need to write a function that can determine if it is height-balanced.

# A height-balanced tree can be defined as a binary tree in which the left and right subtrees of every node differ in height by a maximum of 1.

# Example 1:
# Given the following tree [5,10,25,None,None,12,3]:

#     5
#    / \
#  10  25
#     /  \
#    12   3
# return True.

# Example 2:
# Given the following tree [5,6,6,7,7,None,None,8,8]:

#        5
#       / \
#      6   6
#     / \
#    7   7
#   / \
#  8   8
# return False.

# [execution time limit] 4 seconds (py3)

# [input] tree.integer root

# [output] boolean
# Find the left and right height
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def balancedBinaryTree(root):
    
    def height(root):
        if root is None:
            return 0
        return max(height(root.left), height(root.right)) + 1
        
    def isBalanced(root):
        if root is None:
            return True
        
        lh = height(root.left)
        rh = height(root.right)
        
        if (abs(lh - rh) <= 1) and isBalanced(root.left) is True and isBalanced(root.right) is True:
            return True
            
        return False
    
    value = isBalanced(root)
    return value