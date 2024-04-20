# data_structures/arrays/2d_array.py

class Array2D:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.array = [[None] * cols for _ in range(rows)]

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.array])

    def __getitem__(self, indices):
        row, col = indices
        return self.array[row][col]

    def __setitem__(self, indices, value):
        row, col = indices
        self.array[row][col] = value

    def __len__(self):
        return self.rows

    def insert(self, row, col, value):
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            raise IndexError("Index out of bounds")
        self.array[row][col] = value

    def delete(self, row, col):
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            raise IndexError("Index out of bounds")
        self.array[row][col] = None

    def search(self, value):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.array[i][j] == value:
                    return i, j
        return -1, -1

    def update(self, row, col, value):
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            raise IndexError("Index out of bounds")
        self.array[row][col] = value


# Example usage:
if __name__ == "__main__":
    arr = Array2D(3, 3)
    print("Initial array:")
    print(arr)

    arr.insert(0, 0, 1)
    arr.insert(0, 1, 2)
    arr.insert(0, 2, 3)
    arr.insert(1, 0, 4)
    arr.insert(1, 1, 5)
    arr.insert(1, 2, 6)
    arr.insert(2, 0, 7)
    arr.insert(2, 1, 8)
    arr.insert(2, 2, 9)
    print("\nArray after insertions:")
    print(arr)

    arr.delete(1, 1)
    print("\nArray after deletion at (1, 1):")
    print(arr)

    print("\nIndices of value 5:", arr.search(5))

    arr.update(0, 0, 10)
    print("\nArray after updating value at (0, 0):")
    print(arr)
