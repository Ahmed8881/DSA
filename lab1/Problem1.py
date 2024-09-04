




def SearchIndex(arr,x):
    newarr=[]
    for i in range(len(arr)):
        if(arr[i]==x):
            newarr.append(i)
    return newarr
        

array=[22,2,1,7,11,13,5,2,9]
a=int(input("Enter a num: "))
print(SearchIndex(array,a))        