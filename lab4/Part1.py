def QuickSort(A, p, r):
    # If the array has more than one element
    if p < r:
        # Partition the array and get the pivot index
        q = Partition(A, p, r)
        # Recursively sort the elements before the pivot
        QuickSort(A, p, q-1)
        # Recursively sort the elements after the pivot
        QuickSort(A, q+1, r)

def Partition(A, p, r):
    # Choose the last element as the pivot
    x = A[r]
    # Index of the smaller element
    i = p - 1
    # Traverse through all elements
    for j in range(p, r):
        # If the current element is smaller than or equal to the pivot
        if A[j] <= x:
            # Increment the index of the smaller element
            i = i + 1
            # Swap the elements
            A[i], A[j] = A[j], A[i]
    # Swap the pivot element with the element at i+1
    A[i+1], A[r] = A[r], A[i+1]
    # Return the partition index
    return i + 1

# Example array
A = [2, 8, 7, 1, 3, 5, 6, 4]
# Perform QuickSort on the array
QuickSort(A, 0, len(A) - 1)
# Print the sorted array
print(A)