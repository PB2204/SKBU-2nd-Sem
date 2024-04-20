# data_structures/sorting/bubble.py

def bubble_sort(arr):
    """
    Sorts the given list using bubble sort algorithm.
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


# Example usage:
if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    print("Original array:", arr)
    bubble_sort(arr)
    print("Sorted array:", arr)
