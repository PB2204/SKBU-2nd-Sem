# data_structures/sorting/insertion.py

def insertion_sort(arr):
    """
    Sorts the given list using insertion sort algorithm.
    """
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Example usage:
if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    print("Original array:", arr)
    insertion_sort(arr)
    print("Sorted array:", arr)
