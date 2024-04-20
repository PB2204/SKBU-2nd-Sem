# data_structures/searching/liner_search.py

def linear_search(arr, x):
    """
    Perform linear search to find the index of element x in the array arr.
    If x is not found, return -1.
    """
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


# Example usage:
if __name__ == "__main__":
    arr = [70, 20, 80, 10, 30]

    arr.sort()
    x = 30
    index = linear_search(arr, x)
    if index != -1:
        print(f"Element {x} found at index {index}.")
    else:
        print(f"Element {x} not found in the array.")
