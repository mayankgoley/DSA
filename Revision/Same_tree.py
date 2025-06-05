class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_same_tree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    return p.value == q.value and is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

# Example usage
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
print("Are the two trees the same?", is_same_tree(root1, root2))  # Output: True