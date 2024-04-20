# data_structures/sorting/quick.py

def partition(arr, low, high):
    """
    Partitions the array around a pivot element.
    """
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    """
    Sorts the given list using quick sort algorithm.
    """
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


# Example usage:
if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    n = len(arr)
    print("Original array:", arr)
    quick_sort(arr, 0, n - 1)
    print("Sorted array:", arr)
