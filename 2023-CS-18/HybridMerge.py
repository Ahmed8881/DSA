import funcs
import time
import Insertion as IS


      
def HybridMergeSort(array, start, end):
    n = 10  # for switching to insertion sort
    if start < end:
        if (end - start + 1) > n: 
            mid = (start + end) // 2
            HybridMergeSort(array, start, mid)   
            HybridMergeSort(array, mid + 1, end) 
            funcs.Merge(array, start, mid, end) 
        else:
            IS.InsertionSort(array, start, end + 1)  
    return array

            
if __name__ == "__main__":
    n=30000
    array = funcs.RandomArray(n)
    start = time.perf_counter()
    new=HybridMergeSort(array, 0, n-1)
    end = time.perf_counter()
    print("Time taken to sort the array: ", end - start)
    