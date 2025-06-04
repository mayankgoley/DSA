# implementation of postorder traversal of a binary tree
# using recursion and iteration.

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
def postorder_traversal_recursive(root):
    if root:
        postorder_traversal_recursive(root.left)
        postorder_traversal_recursive(root.right)
        print(root.value, end = " ")

root = TreeNode(10)
root.left = TreeNode(20)
root.right = TreeNode(30)
root.right.left = TreeNode(40)
root.right.right = TreeNode(50)

print("Postorder Traversal (Recursive):", end = " ")
postorder_traversal_recursive(root)
print("\n")