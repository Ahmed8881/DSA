# Problem 1
def SearchA(Arr, x):
    newarr=[]
    for i in range(len(Arr)):
        if(Arr[i]==x):
            newarr.append(i)
    return newarr   
# Driver Code
array=[22,2,1,7,11,13,5,2,9]
a=int(input("Enter a num: "))
print(SearchA(array,a)) 


# Problem 2
def SearchB(Arr, x):
    arr1 = []
    for i in range(len(Arr)):
        if Arr[i] == x:
            arr1 .append(i)
            if (i != len(Arr) - 1 and Arr[i] != Arr[i + 1]):
                break
    return arr1
# Driver Code
array1=[0, 1, 2, 2,2, 6, 7, 8, 9]
a=int(input("Enter a num: "))
print(SearchB(array1,a))

# Problem 3
def Minimum(Arr, starting, ending):
    min=starting
    for i in range(starting,ending+1):
        if(Arr[min]>Arr[i]):
            min=i
    return min

# Driver Code

Array= [-5, -2, 7, 8, 0, 1, 23, 3, 4]
StartingIndex= 2
EndingIndex= 8
print(Minimum(Array,StartingIndex,EndingIndex))
  
  
# Problem 4
def Sort4(Array):
    StartingIndex= 0
    EndingIndex= len(Array) - 1
    for i in range(len(Array)):
        a = Minimum(Array, StartingIndex, EndingIndex)
        b = Array[i]
        Array[i] = Array[a]
        Array[a] = b
        StartingIndex +=1
    return Array
# Driver Code
X=[3,4,7,8,0,1,23,-2,-5] 
print(Sort4(X))

# Problem 5
def StringReverse(str,starting,ending):
    reversed=str[starting:ending+1]
    return reversed[::-1]
    

s = "University of Engineering and Technology Lahore"
a=StringReverse(s,25,9)
print(a)


# Problem 6 
def SumIteratice(number):
    sum=0
    while(number>0):
        sum+=number%10
        number=number//10
    return sum

def SumRecursive(number):
    if number==0:
        return 0
    else:
        return number%10+SumRecursive(number//10)
      
sum1=SumIteratice(111111)
print(sum1)
sum2=SumRecursive(12)
print(sum2)

# Problem 7
matrix=[[1,13,13],[5,11,6],[4,4,9]]



def ColumnWiseSum(matrix):
    sum=0
    arr=[]
    for i in range(0,len(matrix)):
        sum=0
        for j in range(0,len(matrix)):
            sum+=matrix[j][i]
        arr.append(sum)
    return arr

def RowWiseSum(matrix):
    arr=[]
    for i in range(len(matrix)):
        sum=0
        for j in range (len(matrix)):
            sum+=matrix[i][j]
        arr.append(sum)
    return arr
            
    
print(ColumnWiseSum(matrix))
print(RowWiseSum(matrix))
       
# Problem 8
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
A = [0,3,4,-8,-8,10,11] 
B = [1,8,13,24] 
print(SortedMerge(A,B))

# Problem 9
def PalindromRecursive(str):
    Start=0
    End=-1
    if len(str)==0 or len(str)==1:
        return True
    elif(str[Start]!=str[End]):
        return False
    else:
         Start+=1
         End=-Start+1
         return PalindromRecursive(str[Start:-1])
         

s="radar"
print(PalindromRecursive(s))

def Sort10(Arr):
    Arr = Sort4(Arr)
    positive = []
    negative = []
    sortedArray = []
    
    for i in range(len(Arr)):
        if Arr[i] >= 0:
            positive.append(Arr[i])
        else:
            negative.append(Arr[i])
    
    for i in range(len(Arr)):
        if i < len(negative):
            sortedArray.append(negative[i])
        if i < len(positive):
            sortedArray.append(positive[i])
    
    return sortedArray

Arr= [-1,-2,-3,-4,-5,1,2,3,4,5] 
print(Sort10(Arr))


