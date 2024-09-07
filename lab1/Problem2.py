




def SearchIndex(arr,x):
    newarr=[]
    for i in range(len(arr)):
        if(arr[i]==x):
            newarr.append(i)
            if(arr[i]==arr[i+1]):
                newarr.append(i+1)
                break
    return newarr
        
            
        
array1=[0, 1, 2, 2, 5, 6, 7, 8, 9]
array=[22,2,1,7,11,13,5,2,9]
a=int(input("Enter a num: "))
print(SearchIndex(array1,a))        