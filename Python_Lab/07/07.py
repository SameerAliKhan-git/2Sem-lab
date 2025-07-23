# Write a program to sort the elements of the list using merge sort.  


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        # Recursive sorting of both halves
        merge_sort(left)
        merge_sort(right)

        # Merge sorted halves
        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Copy any remaining elements of left[]
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        # Copy any remaining elements of right[]
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

# Example usage:
lst = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print("Original list:", lst)
merge_sort(lst)
print("Sorted list:", lst)



