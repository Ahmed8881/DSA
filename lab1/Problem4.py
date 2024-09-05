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


Array= [0,5,4,2,6,7,8,9,1] 
StartingIndex= 0
EndingIndex= 8
for i in range(len(Array)):
    a=Minimum(Array,StartingIndex,EndingIndex)
    b=Array[i]
    Array[i]=Array[a]
    Array[a]=b
    # Array.pop(a)
    # Array.append(b)
    StartingIndex=StartingIndex+1
print(Array)
    
    
       
        
        


