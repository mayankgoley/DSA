# Find the height of a binary tree

class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def height_of_tree(root):
    if root is None:
        return 0
    left_height = height_of_tree(root.left)
    right_height = height_of_tree(root.right)
    return(max(left_height, right_height) +1 )

# Example usage
root = BinaryTreeNode(10)
root.left = BinaryTreeNode(20)
root.right = BinaryTreeNode(30)
root.left.left = BinaryTreeNode(40)
root.left.right = BinaryTreeNode(50)
root.right.left = BinaryTreeNode(60)
root.right.right = BinaryTreeNode(70)
print("Height of the tree is:", height_of_tree(root))