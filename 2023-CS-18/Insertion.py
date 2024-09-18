import funcs 
import time

# Sort Function

def InsertionSort(array, start, end):
    for i in range(start+1,end,1):
        check = array[i]
        j = i - 1
        while j >= start and array[j] > check:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = check
    return array

if __name__ == "__main__":
    n=30000
    array=funcs.RandomArray(n)
    start_time=time.perf_counter()
    new=InsertionSort(array,0,n)
    end_time=time.perf_counter()
    run_time=end_time-start_time
    funcs.WriteFiles(" SortedInsertionSort.csv", new)  


    
    