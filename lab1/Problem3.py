def Minimum(Arr,start,End):
    min=start
    for i in range(start,End+1):
        if(Arr[start]>Arr[i]):
            min=i
    return min
        
                
               
    

        
Array= [3,4,7,8,0,1,23,-2,-5] 
StartingIndex= 4 
EndingIndex= 7 
print(Minimum(Array,StartingIndex,EndingIndex))
