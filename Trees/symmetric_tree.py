"""
You're given the root of a binary tree.
Check if the tree is a mirror of itself (i.e., symmetric around its center)."""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_symmetric_tree(root):
    if root is None:
        return True
    def is_mirror(t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return (t1.value == t2.value and 
                is_mirror(t1.left, t2.right) and
                is_mirror(t1.right, t2.left))
    return is_mirror(root.left, root.right)

# Example usage
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)
print("Is the tree symmetric?", is_symmetric_tree(root))  # Output: True
        
        

