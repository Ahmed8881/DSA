import funcs
import time


# Sort Function
def SelectionSort(array,start,end):
    for i in range(start,end):
        minimum=i
        # print("i=",i,array)
        for j in range(i+1,end):
            if(array[j]<array[minimum]):
                minimum=j
                print('i=',i,'j=',j,array)
        array[i],array[minimum]=array[minimum],array[i]
        print('swapped',array)
    return array

A=[5,7,3,9,1]
print(SelectionSort(A,0,5))

# Driver Code
# if __name__=="__main__":
#     n=30000
#     array=funcs.RandomArray(n)
#     start_time=time.perf_counter()
#     new=SelectionSort(array,0,n)
#     end_time=time.perf_counter()
#     run_time=end_time-start_time
#     print("Run time of SelectionSort at", n,"is",run_time,"seconds")
#     print(funcs.isSorted(array,0,n))
#     funcs.WriteFiles(" SortedSelectionSort.csv", new)  
    