# Given a binary tree of integers, return all the paths from the tree's root to its leaves as an array of strings. The strings should have the following format:
# "root->node1->node2->...->noden", representing the path from root to noden, where root is the value stored in the root and node1,node2,...,noden are the values stored in the 1st, 2nd,..., and nth nodes in the path respectively (noden representing the leaf).

# Example

# For

# t = {
#     "value": 5,
#     "left": {
#         "value": 2,
#         "left": {
#             "value": 10,
#             "left": null,
#             "right": null
#         },
#         "right": {
#             "value": 4,
#             "left": null,
#             "right": null
#         }
#     },
#     "right": {
#         "value": -3,
#         "left": null,
#         "right": null
#     }
# }
# the output should be
# treePaths(t) = ["5->2->10", "5->2->4", "5->-3"].

# The given tree looks like this:

#     5
#    / \
#   2  -3
#  / \
# 10  4
#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def treePaths(t):

    def paths(root, pathlist):
        if root is None:
            return
        if root is not None:
            value = root.value
            pathlist.append(str(value))
            paths(root.left, pathlist)
    
    def preOrder(root, result):
        pathlist = []
        paths(root, pathlist)
        c = "->"
        s = c.join(pathlist)
        if len(pathlist) > 0:
            value = result.append(s)
            tryit = preOrder(root.left, result)
            return value
        
    def queStack(root):
        result = []
        preOrder(root, result)
        print("questack", result)
        
    queStack(t)
# que each string result 