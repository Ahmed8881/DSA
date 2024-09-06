
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


Array=  [10, -1, 9, 20, -3, -8, 22, 9, 7] 
StartingIndex= 0
EndingIndex= 8
lenght=len(Array)
for i in range(lenght):
    a=Minimum(Array,StartingIndex,EndingIndex)
    if(Array[a]<0):
        b=Array[i]
        Array[i]=Array[a]
        Array[a]=b
        StartingIndex=StartingIndex+1
        lenght+=2
    if(Array[i]>0):
        b=Array[i]
        Array[i]=Array[a]
        Array[a]=b
        StartingIndex=StartingIndex+1
print(Array)
    
    
       
        
        


        