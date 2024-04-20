# data_structures/trees_and_graphs/dfs_trees.py

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def dfs_traversal(root):
    if not root:
        return []

    result = []
    stack = []
    stack.append(root)

    while stack:
        node = stack.pop()
        result.append(node.key)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result


# Example usage:
if __name__ == "__main__":
    # Constructing a binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    print("DFS traversal of the binary tree:")
    print(dfs_traversal(root))  # Output: [1, 2, 4, 5, 3, 6, 7]
