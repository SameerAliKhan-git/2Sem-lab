# 1. DEFINE THE FUNCTIONS

def partition(arr, low, high):
    """
    Takes the last element as pivot and places it correctly.
    """
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    """
    The main Quick Sort function.
    """
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

# 2. CREATE A LIST AND CALL THE FUNCTION

# This is the list you want to sort
my_list = [8, 3, 2, 9, 7, 1, 5, 4]
n = len(my_list)

print(f"Original list: {my_list}")

# Call quick_sort with the correct arguments:
# arr -> your list
# low -> starting index (0)
# high -> ending index (length of list - 1)
quick_sort(my_list, 0, n - 1)

print(f"Sorted list:   {my_list}")

