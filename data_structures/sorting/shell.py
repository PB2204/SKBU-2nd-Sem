# data_structures/sorting/shell.py

def shell_sort(arr):
    """
    Sorts the given list using shell sort algorithm.
    """
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2


# Example usage:
if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    print("Original array:", arr)
    shell_sort(arr)
    print("Sorted array:", arr)
