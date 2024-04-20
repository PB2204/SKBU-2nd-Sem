# data_structures/trees_and_graphs/tree_traversals.py

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

    def inorder_traversal(self):
        return self._inorder_traversal(self.root, [])

    def _inorder_traversal(self, node, result):
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.data)
            self._inorder_traversal(node.right, result)
        return result

    def preorder_traversal(self):
        return self._preorder_traversal(self.root, [])

    def _preorder_traversal(self, node, result):
        if node:
            result.append(node.data)
            self._preorder_traversal(node.left, result)
            self._preorder_traversal(node.right, result)
        return result

    def postorder_traversal(self):
        return self._postorder_traversal(self.root, [])

    def _postorder_traversal(self, node, result):
        if node:
            self._postorder_traversal(node.left, result)
            self._postorder_traversal(node.right, result)
            result.append(node.data)
        return result


# Example usage:
if __name__ == "__main__":
    binary_tree = BinaryTree(5)
    binary_tree.insert(3)
    binary_tree.insert(7)
    binary_tree.insert(1)
    binary_tree.insert(4)
    binary_tree.insert(6)
    binary_tree.insert(9)

    # Output: In-order traversal: [1, 3, 4, 5, 6, 7, 9]
    print("In-order traversal:", binary_tree.inorder_traversal())
    # Output: Pre-order traversal: [5, 3, 1, 4, 7, 6, 9]
    print("Pre-order traversal:", binary_tree.preorder_traversal())
    # Output: Post-order traversal: [1, 4, 3, 6, 9, 7, 5]
    print("Post-order traversal:", binary_tree.postorder_traversal())
