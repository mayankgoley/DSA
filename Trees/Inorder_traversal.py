# Implement inorder traversal of a binary tree using recursion and iteration.

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inorder_traversal_recursive(root):
    if root:
        inorder_traversal_recursive(root.left)
        print(root.value, end  = " ")
        inorder_traversal_recursive(root.right)


root = TreeNode(10)
root.left = TreeNode(20)
root.right = TreeNode(30)
root.right.left = TreeNode(40)
root.right.right = TreeNode(50)

print("Inorder Traversal (Recursive):", end = " ")
inorder_traversal_recursive(root)
print("\n") 
