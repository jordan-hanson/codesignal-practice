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
        print("line 13", root.value)
        if root.left is None and root.right is not None:
            value = root.value
            pathlist.append(str(value))
            paths(root.right, pathlist)
        if root.right is None and root.left is not None:
            value = root.value
            pathlist.append(str(value))
            paths(root.left, pathlist)
        if root.left is None and root.right is None:
            value = root.value
            pathlist.append(str(value))
        if root is not None:
            value = root.value
            pathlist.append(str(value))
            paths(root.left, pathlist)
            print("line 17", pathlist)
            # pathlist.append(str(value))
            paths(root.right, pathlist)
            print("line 19", pathlist)
            # pathlist.append(str(value))
    
    def preOrder(root, result):
        pathlist = []
        paths(root, pathlist)
        c = "->"
        s = c.join(pathlist)
        print(pathlist)
        print(result)
        if len(pathlist) > 0:
            value = result.append(s)
            # tryit = preOrder(root.left, result)
            # tryitl = preOrder(root.right, result)
            return value
        
    def queStack(root):
        result = []
        preOrder(root, result)
        print("questack", result)
        
    queStack(t)
# que each string result 

def treePaths(t):

    if not t or t.value == None:
        return None
        
    def findPath(node, subpaths = []):
        current = []
        if node.left:
            paths = findPath(node.left)
            for i in range(len(paths)):
                current.append(str(node.value) + "->" + paths[i])
        if node.right:
            paths = findPath(node.right)
            for i in range(len(paths)):
                current.append(str(node.value) + "->" + paths[i])
        if node.left is None or node.right is None:
            current.append(str(node.value))
        if node == None:
            return current
        return current
    
    results = findPath(t)
    return results