def linear_search(arr, target):
    for x in arr:
        if x == target:
            return arr.index(x)

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    arr.sort()
    while high >= low:
        middle = (low + high) // 2
        if arr[middle] == target:
            return middle
        elif arr[middle] < target:
            low = middle + 1
        elif arr[middle] > target:
            high = middle - 1

    return -1  # not found
