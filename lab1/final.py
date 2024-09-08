# Problem 1
def SearchA(Arr, x):
    newarr=[]
    for i in range(len(Arr)):
        if(Arr[i]==x):
            newarr.append(i)
    return newarr   
# Driver Code
# array=[22,2,1,7,11,13,5,2,9]
# a=int(input("Enter a num: "))
# print(SearchA(array,a)) 


# Problem 2
def SearchB(arr, x):
    arr1 = []
    for i in range(len(arr)):
        if arr[i] == x:
            arr1 .append(i)
            if i != len(arr) - 1 and arr[i] != arr[i + 1]:
                break
    return arr1
# Driver Code
array1=[0, 1, 2, 2,2, 6, 7, 8, 9]
a=int(input("Enter a num: "))
print(SearchB(array1,a))

# Problem 3
def Minimum(Arr,start,End):
    min=start
    for i in range(start,End+1):
        if(Arr[min]>Arr[i]):
            min=i
    return min

# Driver Code

Array= [-5, -2, 7, 8, 0, 1, 23, 3, 4]
StartingIndex= 2
EndingIndex= 8
print(Minimum(Array,StartingIndex,EndingIndex))
  