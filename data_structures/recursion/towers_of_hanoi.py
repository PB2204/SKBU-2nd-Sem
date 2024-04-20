# data_structures/recursion/towers_of_hanoi.py

class TowersOfHanoi:
    def __init__(self):
        self.moves = []

    def hanoi(self, n, source, auxiliary, target):
        if n == 1:
            self.moves.append((source, target))
            return
        self.hanoi(n - 1, source, target, auxiliary)
        self.moves.append((source, target))
        self.hanoi(n - 1, auxiliary, source, target)

    def get_moves(self):
        return self.moves

    def reset_moves(self):
        self.moves = []


# Example usage:
if __name__ == "__main__":
    towers_of_hanoi = TowersOfHanoi()
    towers_of_hanoi.hanoi(3, 'A', 'B', 'C')
    print("Moves to solve Towers of Hanoi with 3 disks:")
    # Output: Moves to solve Towers of Hanoi with 3 disks: [('A', 'C'), ('A', 'B'), ('C', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('A', 'C')]
    print(towers_of_hanoi.get_moves())
