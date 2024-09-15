import funcs
import time

def MergeSort(array, start, end):
    mid = start + (end-start) // 2
    if len(array) == 1:
        return array
    if start < end:
        MergeSort(array, start, mid)
        MergeSort(array, mid + 1, end)
    funcs.Merge(array, start, mid, end)
    
if __name__ == "__main__":
    n=30000
    array = funcs.RandomArray(n)
    start = time.perf_counter()
    MergeSort(array, 0, n-1)
    end = time.perf_counter()
    print(funcs.isSorted(array, 0, 16))
    print("Time taken to sort the array: ", end - start)
    funcs.WriteFiles("SortedMergeSort.csv", array)