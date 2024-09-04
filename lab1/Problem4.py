def Minimum(Arr,start,End):
    min=start
    for i in range(start,End+1):
        if(Arr[start]>Arr[i]):
            min=i
    return min

    
    
    
Array= [3,4,7,8,0,1,23,-2,-5] 
StartingIndex= 0
EndingIndex= 8
for i in range(len(Array)):
        a=Minimum(Array,StartingIndex,EndingIndex)
        b=Array[i]
        Array[i]=Array[a]
        Array.pop(a)
        Array.append(b)
       
        
        
print(Array)    


