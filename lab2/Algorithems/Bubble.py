import funcs
import time

# Sort Function
def BubbleSort(array,start,end):
    check=False
    for i in range(start,end-1):
        for j in range(start,end-1-i):
            if(array[j]>array[j+1]):
                check=True
                array[j],array[j+1]=array[j+1],array[j]
        if not check:
            break
    return array

if __name__=="__main__":
    n = 30000
    array = funcs.RandomArray(n)
    start_time=time.perf_counter()
    new_array=BubbleSort(array,0,n)
    end_time=time.perf_counter()
    run_time=end_time-start_time
    funcs.WriteFiles("SortedBubbleSort.csv", new_array)  
    print(funcs.isSorted(new_array,0,n))
    print("Run time of BubbleSort at", n,"is",run_time,"seconds")