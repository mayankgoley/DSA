class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def print_tree(node, level = 0):
    if node is None:
        return
    print(' ' * level + str(node.value))
    print_tree(node.left, level +1)
    print_tree(node.right, level +1)

    
root = BinaryTreeNode('A')
root.left = BinaryTreeNode('B')
root.right = BinaryTreeNode('C')
root.left.left = BinaryTreeNode('D')
root.left.right = BinaryTreeNode('E')
root.right.left = BinaryTreeNode('F')
root.right.right = BinaryTreeNode('G')
print_tree(root)
