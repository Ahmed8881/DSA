def Minimum(Arr,start,End):
    min=start
    for i in range(start,End+1):
        if(Arr[min]>Arr[i]):
            min=i
    return min



Array= [-5, -2, 7, 8, 0, 1, 23, 3, 4]
StartingIndex= 2
EndingIndex= 8
print(Minimum(Array,StartingIndex,EndingIndex))
  