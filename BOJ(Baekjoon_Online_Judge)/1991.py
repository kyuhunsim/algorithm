class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def preorder_traversal(node):
    if node:
        print(node.key, end="")
        preorder_traversal(node.left)
        preorder_traversal(node.right)

def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.key, end="")
        inorder_traversal(node.right)

def postorder_traversal(node):
    if node:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.key, end="")

def build_binary_tree(n):
    nodes = {}
    for i in range(n):
        node_data = input().split()
        node_key = node_data[0]
        left_child_key = node_data[1]
        right_child_key = node_data[2]

        node = nodes.get(node_key, TreeNode(node_key))

        if left_child_key != ".":
            left_child = nodes.get(left_child_key, TreeNode(left_child_key))
            node.left = left_child
            nodes[left_child_key] = left_child

        if right_child_key != ".":
            right_child = nodes.get(right_child_key, TreeNode(right_child_key))
            node.right = right_child
            nodes[right_child_key] = right_child

        nodes[node_key] = node

    return nodes['A']

if __name__ == "__main__":
    N = int(input())
    root = build_binary_tree(N)
    preorder_traversal(root)
    print()
    inorder_traversal(root)
    print()
    postorder_traversal(root)
