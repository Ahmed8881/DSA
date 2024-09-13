import funcs
import time
def BubbleSort(array,start,end):
    for i in range(start,end-1):
        for j in range(start,end-1-i):
            if(array[j]>array[j+1]):
                array[j],array[j+1]=array[j+1],array[j]
    return array

if __name__=="__main__":
    n = 30000
    array = funcs.RandomArray(n)
    start_time=time.perf_counter()
    new_array=BubbleSort(array,0,30000)
    end_time=time.perf_counter()
    print(funcs.isSorted(new_array,0,30000))
run_time=end_time-start_time
print("Run time of BubbleSort at", n,"is",run_time,"seconds")
 