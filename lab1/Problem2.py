




def SearchIndex(arr,x):
    newarr=[]
    for i in range(len(arr)):
        if(arr[i]==x):
            newarr.append(i)
            if(arr[i]!=arr[i+1] and i!=len(arr)-1):
                break
    return newarr
        
            
        
array1=[0, 1, 2, 2,2, 6, 7, 8, 9]
a=int(input("Enter a num: "))
print(SearchIndex(array1,a))        