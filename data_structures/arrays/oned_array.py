# data_structures/arrays/1d_array.py

class Array1D:
    def __init__(self, size):
        self.size = size
        self.array = [None] * size

    def __str__(self):
        return str(self.array)

    def __getitem__(self, index):
        return self.array[index]

    def __setitem__(self, index, value):
        self.array[index] = value

    def __len__(self):
        return len(self.array)

    def insert(self, index, value):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        self.array[index] = value

    def delete(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        self.array[index] = None

    def search(self, value):
        for i in range(self.size):
            if self.array[i] == value:
                return i
        return -1

    def update(self, index, value):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        self.array[index] = value


# Example usage:
if __name__ == "__main__":
    arr = Array1D(5)
    print("Initial array:", arr)

    arr[0] = 1
    arr[1] = 2
    arr[2] = 3
    arr[3] = 4
    arr[4] = 5
    print("Array after insertions:", arr)

    arr.delete(2)
    print("Array after deletion at index 2:", arr)

    print("Index of value 4:", arr.search(4))

    arr.update(1, 10)
    print("Array after updating value at index 1:", arr)
