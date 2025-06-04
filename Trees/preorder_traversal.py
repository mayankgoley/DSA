# Implement preorder traversal of a binary tree using recursion and iteration.

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
def preorder_traversal_recursive(root):
    if root:
        print(root.value, end = " ")
        preorder_traversal_recursive(root.left)
        preorder_traversal_recursive(root.right)

root = TreeNode(10)
root.left = TreeNode(20)
root.right = TreeNode(30)
root.right.left = TreeNode(40)
root.right.right = TreeNode(50)

print("Preorder Traversal (Recursive):", end = " ")
preorder_traversal_recursive(root)
