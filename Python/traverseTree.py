# Note: Try to solve this task without using recursion, since this is what you'll be asked to do during an interview.

# Given a binary tree of integers t, return its node values in the following format:

# The first element should be the value of the tree root;
# The next elements should be the values of the nodes at height 1 (i.e. the root children), ordered from the leftmost to the rightmost one;
# The elements after that should be the values of the nodes at height 2 (i.e. the children of the nodes at height 1) ordered in the same way;
# Etc.
#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def traverseTree(t):

    if t is None:
        return []

    result = []
    queue = []
    queue.append(t)

    while len(queue) != 0:
        node = queue.pop(0)
        result.append(node.value)

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)

    return result