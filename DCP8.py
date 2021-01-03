# This problem was asked by Google.

# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

# Given the root to a binary tree, count the number of unival subtrees.

# For example, the following tree has 5 unival subtrees:

#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1

class Node:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def countSubTree(root, count):
    if root is None:
        return True
    left = countSubTree(root.left, count)
    right = countSubTree(root.right, count)
    # checking root value and children's values
    if left == False or right == False:
        return False
    if root.left and root.val != root.left.val:
        return False
    if root.right and root.val != root.right.val:
        return False
    # If all the above cases are not true, i.e. if the root value matches with both the children
    # then this case is reached, we increment the count
    count[0] += 1
    return True


def countTrees(root):
    count = [0]
    # calling a new function, to maintain the value of count in recursive calls
    countSubTree(root, count)
    return count[0]


root = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
print("No. of unival subtrees=", countTrees(root))