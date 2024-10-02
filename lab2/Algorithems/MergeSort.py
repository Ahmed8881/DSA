import funcs
import time

# Sort Function

def MergeSort(array, start, end):
    mid = start + (end-start) // 2
    if len(array) == 1:
        return array
    if start < end:
        MergeSort(array, start, mid)
        MergeSort(array, mid + 1, end)
    Merge(array, start, mid, end)
def Merge(array, p, q, r):  
    Left = q - p + 1 
    Right = r - q
    
    L = [0] * Left   
    R = [0] * Right
    
    for i in range(0, Left):
        L[i] = array[p + i]

    for j in range(0, Right):
        R[j] = array[q + 1 + j]
    
    i = 0
    j = 0
    k = p
    
    while i < Left  and j < Right:
        if L[i] <= R[j]:
            array[k] = L[i]
            i+=1
        else:
            array[k] = R[j]
            j+=1
        k+=1
    
    while i<Left:
        array[k] = L[i]
        i+=1
        k+=1

    while j<Right:
        array[k] = R[j]
        j+=1
        k+=1
    print(array)
 
if __name__ == "__main__":
    A=[5,7,3,9,1]
    print(MergeSort(A, 0, len(A)-1))
    # n=10
    # array = funcs.RandomArray(n)
    
    # start = time.perf_counter()
    # MergeSort(array, 0, n-1)
    # end = time.perf_counter()
    # print(funcs.isSorted(array, 0, 16))
    # print("Time taken to sort the array: ", end - start)
    # funcs.WriteFiles("SortedMergeSort.csv", array)