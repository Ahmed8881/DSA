import funcs
import time
import Insertion as IS


def HybridMergeSort(array, start, end):
    mid = start + (end-start) // 2
    if len(array) == 1:
        return array
    if start < end:
        if end - start < 16:
           IS.InsertionSort(array, start, end)
        else:
            HybridMergeSort(array, start, mid)
            HybridMergeSort(array, mid + 1, end)
        funcs.Merge(array, start, mid, end)
            
if __name__ == "__main__":
    n=30000
    array = funcs.RandomArray(n)
    start = time.perf_counter()
    HybridMergeSort(array, 0, n-1)
    end = time.perf_counter()
    print(funcs.isSorted(array, 0, n-1))
    print("Time taken to sort the array: ", end - start)
   