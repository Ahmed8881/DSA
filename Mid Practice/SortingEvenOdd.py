def BubbleSort(array,start,end):
    even=[]
    odd=[]
    for i in range(len(array)):
        if(i%2==0):
            even.append(array[i])
        else:
            odd.append(array[i])

    for i in range(len(even)):
        for j in range(0,len(even)-i-1):
            if(even[j]>even[j+1]):
                even[j],even[j+1]=even[j+1],even[j]
    for i in range(0,len(array)):
        if i%2==0:
            array[i]=even.pop(0)
        else:
            array[i]=odd.pop(0)
    return array
def SelectionSort(array):
    n=len(array)
    even=[]
    odd=[]
    for i in range(len(array)):
        if(i%2==0):
            even.append(array[i])
        else:
            odd.append(array[i])
    for i in range(0,len(even)-1):
        min=i
        for j in range(i+1,len(even)):
            if(even[j]<even[min]):
                min=j
        even[i],even[min]=even[min],even[i]
    for i in range(0,len(array)):
        if i%2==0:
            array[i]=even.pop(0)
        else:
            array[i]=odd.pop(0)
    return array
def InsertionSort(array):
    even=[]
    odd=[]
    for i in range(len(array)):
        if(i%2==0):
            even.append(array[i])
        else:
            odd.append(array[i])
    n=len(even)
    for i in range(1,n):
        key=even[i]
        j=i-1
        while(j>=0 and even[j]>=key):
            even[j+1]=even[j]
            j-=1
        even[j+1]=key
    for i in range(0,len(array)):
        if i%2==0:
            array[i]=even.pop(0)
        else:
            array[i]=odd.pop(0)
    return array
    #quicksort sort only even indexes
def QuickSort(Arry, start, end):
    if start >= end:
        return
    pivot = Arry[end]
    i = start
    j = end - 1
    while i <= j:
        while i <= j and Arry[i] <= pivot:
            i += 2
        while i <= j and Arry[j] >= pivot:
            j -= 2
        if i < j:
            Arry[i], Arry[j] = Arry[j], Arry[i]
    Arry[i], Arry[end] = Arry[end], Arry[i]
    QuickSort(Arry, start, i - 2)
    QuickSort(Arry, i + 2, end)
    return Arry

    

if __name__ == '__main__':
    arr = [11, 21, 3, 42, 15, 6, 5]
    print(QuickSort(arr, 0, len(arr)-1))
        
