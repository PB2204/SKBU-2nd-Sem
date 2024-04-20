# data_structures/arrays/3d_array.py

class Array3D:
    def __init__(self, depth, rows, cols):
        self.depth = depth
        self.rows = rows
        self.cols = cols
        self.array = [
            [[None] * cols for _ in range(rows)] for _ in range(depth)]

    def __str__(self):
        return '\n\n'.join(['\n'.join([' '.join(map(str, row)) for row in layer]) for layer in self.array])

    def __getitem__(self, indices):
        depth, row, col = indices
        return self.array[depth][row][col]

    def __setitem__(self, indices, value):
        depth, row, col = indices
        self.array[depth][row][col] = value

    def __len__(self):
        return self.depth

    def insert(self, depth, row, col, value):
        if depth < 0 or depth >= self.depth or row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            raise IndexError("Index out of bounds")
        self.array[depth][row][col] = value

    def delete(self, depth, row, col):
        if depth < 0 or depth >= self.depth or row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            raise IndexError("Index out of bounds")
        self.array[depth][row][col] = None

    def search(self, value):
        for d in range(self.depth):
            for i in range(self.rows):
                for j in range(self.cols):
                    if self.array[d][i][j] == value:
                        return d, i, j
        return -1, -1, -1

    def update(self, depth, row, col, value):
        if depth < 0 or depth >= self.depth or row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            raise IndexError("Index out of bounds")
        self.array[depth][row][col] = value


# Example usage:
if __name__ == "__main__":
    arr = Array3D(2, 2, 2)
    print("Initial array:")
    print(arr)

    arr.insert(0, 0, 0, 1)
    arr.insert(0, 0, 1, 2)
    arr.insert(0, 1, 0, 3)
    arr.insert(0, 1, 1, 4)
    arr.insert(1, 0, 0, 5)
    arr.insert(1, 0, 1, 6)
    arr.insert(1, 1, 0, 7)
    arr.insert(1, 1, 1, 8)
    print("\nArray after insertions:")
    print(arr)

    arr.delete(0, 0, 1)
    print("\nArray after deletion at (0, 0, 1):")
    print(arr)

    print("\nIndices of value 4:", arr.search(4))

    arr.update(0, 1, 1, 10)
    print("\nArray after updating value at (0, 1, 1):")
    print(arr)
