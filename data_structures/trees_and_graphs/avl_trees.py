# data_structures/trees_and_graphs/avl_trees.py

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        print("Inserting key:", key)
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if not node:
            return TreeNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)
        node.height = 1 + max(self._height(node.left), self._height(node.right))
        balance = self._balance(node)
        if balance > 1 and key < node.left.key:
            print("Performing right rotation on node:", node.key)
            return self._rotate_right(node)
        if balance < -1 and key > node.right.key:
            print("Performing left rotation on node:", node.key)
            return self._rotate_left(node)
        if balance > 1 and key > node.left.key:
            print("Performing left-right rotation on node:", node.key)
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if balance < -1 and key < node.right.key:
            print("Performing right-left rotation on node:", node.key)
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        return node

    def delete(self, key):
        print("Deleting key:", key)
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if not node:
            return node
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if not node.left or not node.right:
                temp = node.left if node.left else node.right
                node = None
                return temp
            temp = self._min_value_node(node.right)
            node.key = temp.key
            node.right = self._delete(node.right, temp.key)
        if not node:
            return node
        node.height = 1 + max(self._height(node.left), self._height(node.right))
        balance = self._balance(node)
        if balance > 1 and self._balance(node.left) >= 0:
            print("Performing right rotation on node:", node.key)
            return self._rotate_right(node)
        if balance < -1 and self._balance(node.right) <= 0:
            print("Performing left rotation on node:", node.key)
            return self._rotate_left(node)
        if balance > 1 and self._balance(node.left) < 0:
            print("Performing left-right rotation on node:", node.key)
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if balance < -1 and self._balance(node.right) > 0:
            print("Performing right-left rotation on node:", node.key)
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        return node

    def _height(self, node):
        if not node:
            return 0
        return node.height

    def _balance(self, node):
        if not node:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self._height(z.left), self._height(z.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))
        return y

    def _rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self._height(y.left), self._height(y.right))
        x.height = 1 + max(self._height(x.left), self._height(x.right))
        return x

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

# Example usage:
if __name__ == "__main__":
    avl_tree = AVLTree()
    avl_tree.insert(10)
    avl_tree.insert(20)
    avl_tree.insert(30)
    avl_tree.insert(40)
    avl_tree.insert(50)
    avl_tree.insert(25)

    avl_tree.delete(30)