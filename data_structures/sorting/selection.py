# data_structures/sorting/selection.py

def selection_sort(arr):
    """
    Sorts the given list using selection sort algorithm.
    """
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


# Example usage:
if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    print("Original array:", arr)
    selection_sort(arr)
    print("Sorted array:", arr)
