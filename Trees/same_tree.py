"""
You are given two binary trees.
Check if they are exactly the same — meaning both:

Have the same structure
Have the same node values at every position"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_same_trees(tree1, tree2):
    if not tree1 and not tree2:
        return True
    if not tree1 or not tree2:
        return False
    if tree1.value != tree2.value:
        return False
    return (is_same_trees(tree1.left, tree2.left) and is_same_trees(tree1.right, tree2.right))

# Example usage
tree1 = TreeNode(1)
tree1.left = TreeNode(2)
tree1.right = TreeNode(3)
tree2 = TreeNode(1)
tree2.left = TreeNode(2)
tree2.right = TreeNode(3)
print("Are the trees same?", is_same_trees(tree1, tree2))  # Output: True