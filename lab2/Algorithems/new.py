def QuickSort(A, p, r):
    if p < r:
        q = Partition(A, p, r)
        QuickSort(A, p, q-1)
        QuickSort(A, q+1, r)
    return A

def Partition(A, p, r):
    # Choose the last element as the pivot
    x = A[r]
    i = p - 1
    for j in range(p, r):
        print(A)
        # If the current element is smaller than or equal to the pivot
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
            print(A)
    A[i+1], A[r] = A[r], A[i+1]
    print(A)
    
    return i + 1



A=[5,7,3,9,1]
print(QuickSort(A, 0, len(A)-1))