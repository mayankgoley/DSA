class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    

def inorder_t(root):
    if root:
        inorder_t(root.left)
        print(root.data, end = " ")
        inorder_t(root.right)


root = TreeNode(10)
root.left = TreeNode(20)
root.right = TreeNode(30)
root.right.left = TreeNode(40)
root.right.right = TreeNode(50)
print("Inorder Traversal:", end = " ")
inorder_t(root)