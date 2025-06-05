class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def invert_tree(root):
    if root is None:
        return None
    

    left = invert_tree(root.left)
    right = invert_tree(root.right)

    root.left = right
    root.right = left

    return root

def print_tree(root, level = 0):
    if root:
        print(" " * level + str(root.value))
        print_tree(root.left, level +1)
        print_tree(root.right, level +1)

    


# Example usage:
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(20)
print_tree(root)
inverted_root = invert_tree(root)
print_tree(inverted_root)