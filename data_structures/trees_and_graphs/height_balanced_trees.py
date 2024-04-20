# data_structures/trees_and_graphs/height_balanced_trees.py

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class HeightBalancedTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if not node:
            return TreeNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return self.balance(node)

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
                node.right = self._delete(node.right, min_node.key)
        return self.balance(node)

    def _find_min(self, node):
        while node.left:
            node = node.left
        return node

    def height(self, node):
        if not node:
            return -1
        return 1 + max(self.height(node.left), self.height(node.right))

    def balance_factor(self, node):
        return self.height(node.left) - self.height(node.right)

    def balance(self, node):
        if self.balance_factor(node) > 1:
            if self.balance_factor(node.left) < 0:
                node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        elif self.balance_factor(node) < -1:
            if self.balance_factor(node.right) > 0:
                node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        return node

    def rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        return new_root

    def rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        return new_root


# Example usage:
if __name__ == "__main__":
    hb_tree = HeightBalancedTree()
    hb_tree.insert(5)
    hb_tree.insert(3)
    hb_tree.insert(7)
    hb_tree.insert(2)
    hb_tree.insert(4)
    hb_tree.insert(6)
    hb_tree.insert(8)

    # Output: Height of the tree: 2
    print("Height of the tree:", hb_tree.height(hb_tree.root))
