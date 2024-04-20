# data_structures/trees_and_graphs/trees.py

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        self.children = [c for c in self.children if c != child]


class Tree:
    def __init__(self, root_data):
        self.root = TreeNode(root_data)

    def print_tree(self):
        self._print_tree(self.root, 0)

    def _print_tree(self, node, level):
        print(" " * (level * 4) + "|___", node.data)
        for child in node.children:
            self._print_tree(child, level + 1)


# Example usage:
if __name__ == "__main__":
    tree = Tree("A")
    b = TreeNode("B")
    c = TreeNode("C")
    d = TreeNode("D")
    e = TreeNode("E")
    f = TreeNode("F")

    tree.root.add_child(b)
    tree.root.add_child(c)
    b.add_child(d)
    b.add_child(e)
    c.add_child(f)

    tree.print_tree()
