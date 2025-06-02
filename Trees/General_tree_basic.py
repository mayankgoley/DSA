class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def print_trees(node, level = 0):
        if node is None:
            return
        print(' ' * level + str(node.value))
        for child in node.children:
            TreeNode.print_trees(child, level +1)



root = TreeNode('A')
node_b = TreeNode('B')
node_c = TreeNode('C')
node_d = TreeNode('D')
node_e = TreeNode('E')
node_f = TreeNode('F')

root.children.extend([node_b, node_c])
node_b.children.extend([node_d, node_e])
node_c.children.append(node_f)

TreeNode.print_trees(root)