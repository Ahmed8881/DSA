# def Minimum(Arr,start,End):
#     min=start
#     for i in range(start,End+1):
#        for j in range(start,End+1):
#            if(Arr[i]>Arr[j]):
#                min=j
#     return min

# Array= [3,4,7,8,0,1,23,-2,-5] 
# StartingIndex= 0
# EndingIndex= 8
# for i in range(len(Array)):
#         a=Minimum(Array,StartingIndex,EndingIndex)
#         print(a)
#         b=Array[i]
#         Array[i]=Array[a]
#         Array.pop(a)    
#         Array.append(b)
#         StartingIndex+=1
#         print(Array)


def Minimum(Arr,start,End):
    min=start
    for i in range(start,End+1):
        if(Arr[min]>=Arr[i]):
            min=i
    return min

def SortedMerge(Arr1, Arr2) :
    StartingIndex=0
    for i in range(len(Arr2)):
      Arr1.append(Arr2[i])
    for j in range(len(Arr1)):
        a=Minimum(Arr1,StartingIndex,len(Arr1)-1)
        b=Arr1[j]
        Arr1[j]=Arr1[a]
        Arr1[a]=b
        StartingIndex=StartingIndex+1
    return Arr1
A = [0,3,4,10,11] 
B = [1,8,13,24] 
print(SortedMerge(A,B))

    
        
        
        
        
        
        
        
        
        


    
       
        
        


