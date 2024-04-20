# data_structures/searching/binary_search.py

def binary_search(arr, x):
    """
    Perform binary search to find the index of element x in the sorted array arr.
    If x is not found, return -1.
    """
    # Sort the array in ascending order
    arr.sort()

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# Example usage:
if __name__ == "__main__":
    arr = [80, 20, 70, 30, 50]
    x = 30

    # Sorting the array before performing binary search
    arr.sort()
    print("Sorted array:", arr)

    index = binary_search(arr, x)
    if index != -1:
        print(f"Element {x} found at index {index}.")
    else:
        print(f"Element {x} not found in the array.")