# data_structures/trees_and_graphs/binary_search_trees.py

class TreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        if not self.root:
            self.root = TreeNode(key, value)
        else:
            self._insert(self.root, key, value)

    def _insert(self, node, key, value):
        if key < node.key:
            if not node.left:
                node.left = TreeNode(key, value)
            else:
                self._insert(node.left, key, value)
        elif key > node.key:
            if not node.right:
                node.right = TreeNode(key, value)
            else:
                self._insert(node.right, key, value)
        else:
            node.value = value  # Update value if key already exists

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if not node:
            return None
        elif node.key == key:
            return node.value
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if not node:
            return node
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                min_node = self._find_min(node.right)
                node.key = min_node.key
                node.value = min_node.value
                node.right = self._delete(node.right, min_node.key)
        return node

    def _find_min(self, node):
        while node.left:
            node = node.left
        return node


# Example usage:
if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(5, "apple")
    bst.insert(3, "banana")
    bst.insert(7, "orange")

    # Output: Search for key 3: banana
    print("Search for key 3:", bst.search(3))

    bst.delete(3)
    # Output: Search for key 3 after deletion: None
    print("Search for key 3 after deletion:", bst.search(3))
