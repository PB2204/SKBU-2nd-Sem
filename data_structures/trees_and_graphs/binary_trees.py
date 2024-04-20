# data_structures/trees_and_graphs/binary_trees.py

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root_data):
        self.root = BinaryTreeNode(root_data)

    def insert(self, data):
        if not self.root:
            self.root = BinaryTreeNode(data)
        else:
            self._insert(self.root, data)

    def _insert(self, node, data):
        if data < node.data:
            if not node.left:
                node.left = BinaryTreeNode(data)
            else:
                self._insert(node.left, data)
        elif data > node.data:
            if not node.right:
                node.right = BinaryTreeNode(data)
            else:
                self._insert(node.right, data)

    def search(self, data):
        return self._search(self.root, data)

    def _search(self, node, data):
        if not node:
            return False
        elif node.data == data:
            return True
        elif data < node.data:
            return self._search(node.left, data)
        else:
            return self._search(node.right, data)


# Example usage:
if __name__ == "__main__":
    binary_tree = BinaryTree(5)
    binary_tree.insert(3)
    binary_tree.insert(7)
    binary_tree.insert(1)
    binary_tree.insert(4)
    binary_tree.insert(6)
    binary_tree.insert(9)

    print("Search for 4:", binary_tree.search(4))  # Output: Search for 4: True
    # Output: Search for 8: False
    print("Search for 8:", binary_tree.search(8))
