def merge_sort(arr):
    """
    Sorts a list in ascending order using the Merge Sort algorithm.

    Args:
        arr: The list of items to be sorted.
    
    Returns:
        The sorted list.
    """
    # The base case: A list with 0 or 1 item is already sorted.
    if len(arr) > 1:
        # 1. DIVIDE Step
        mid = len(arr) // 2  # Find the middle of the list
        left_half = arr[:mid]  # Divide the list into two halves
        right_half = arr[mid:]

        # Recursively call merge_sort on both halves
        merge_sort(left_half)
        merge_sort(right_half)

        # 2. CONQUER (Merge) Step
        i = 0  # Index for the left half
        j = 0  # Index for the right half
        k = 0  # Index for the main list (arr)

        # Copy data from the two halves back to the main list
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Check for any remaining elements in the left half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Check for any remaining elements in the right half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
            
    return arr

# --- Example Usage ---
my_list = [8, 3, 2, 9, 7, 1, 5, 4]
print(f"Original list: {my_list}")

sorted_list = merge_sort(my_list)
print(f"Sorted list:   {sorted_list}")