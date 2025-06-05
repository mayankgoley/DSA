class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end = " ")
        inorder_traversal(root.right)

def preorder_traversal(root):
    if root:
        print(root.value, end = " ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.value, end = " ")

def height_tree(root):
    if root is None:
        return 0
    left_height = height_tree(root.left)
    right_height = height_tree(root.right)
    return max(left_height, right_height) +1

def is_symmetric_tree(root):
    if root is None:
        return True
    def is_mirror(t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        if t1.value != t2.value:
            return False
        return (is_mirror(t1.left, t2.right)
                and is_mirror(t1.right, t2.left))
    return is_mirror(root.left, root.right)

root = TreeNode(10)
root.left = TreeNode(20)
root.right = TreeNode(30)
root.right.left = TreeNode(40)
root.right.right = TreeNode(50)
print("Inorder Traversal:", end = " ")
inorder_traversal(root)
print("\nPreorder Traversal:", end = " ")
preorder_traversal(root)
print("\nPostorder Traversal:", end = " ")
postorder_traversal(root)
print("\n")
print("Height of the tree is:", height_tree(root))

print("Is the tree symmetric?", is_symmetric_tree(root))