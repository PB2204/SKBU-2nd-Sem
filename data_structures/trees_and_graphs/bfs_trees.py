# data_structures/trees_and_graphs/bfs_trees.py

from collections import deque


class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def bfs_traversal(root):
    if not root:
        return []

    result = []
    queue = deque()
    queue.append(root)

    while queue:
        node = queue.popleft()
        result.append(node.key)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

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

    print("BFS traversal of the binary tree:")
    print(bfs_traversal(root))  # Output: [1, 2, 3, 4, 5, 6, 7]
