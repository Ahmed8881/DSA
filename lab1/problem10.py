def Minimum(Arr,start,End):
    min=start
    for i in range(start,End+1):
        if(Arr[min]>=Arr[i]):
            min=i
    return min


Array= [0,5,4,2,6,7,8,9,1] 
def Sort(Arr):
    StartingIndex= 0
    EndingIndex= 8
    for i in range(len(Arr)):
        a=Minimum(Arr,StartingIndex,EndingIndex)
        b=Arr[i]
        Arr[i]=Arr[a]
        Arr[a]=b
        StartingIndex=StartingIndex+1
    return Arr

def Sort10(Arr):
    Arr = Sort(Arr)
    positive = []
    negative = []
    sortedArray = []
    
    for i in range(len(Arr)):
        if Arr[i] >= 0:
            positive.append(Arr[i])
        else:
            negative.append(Arr[i])
    
    for i in range(len(Arr)):
        if i < len(negative):
            sortedArray.append(negative[i])
        if i < len(positive):
            sortedArray.append(positive[i])
    
    return sortedArray

Arr= [-1,-2,-3,-4,-5,1,2,3,4,5] 
print(Sort10(Arr))