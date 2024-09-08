
# Problem 1
def SearchIndex(arr,x):
    newarr=[]
    for i in range(len(arr)):
        if(arr[i]==x):
            newarr.append(i)
    return newarr
# Problem 2
def SearchIndex(arr,x):
    newarr=[]
    for i in range(len(arr)):
        if(arr[i]==x):
            newarr.append(i)
            if(arr[i]==arr[i+1]):
                newarr.append(i+1)
                break
    return newarr


# Problem 3
def Minimum(Arr, start, End):
    min = start
    for i in range(start, End + 1):
        if Arr[min] > Arr[i]:
            min = i
    return min

# Problem 4
def Sort(Arr):
    StartingIndex = 0
    EndingIndex = len(Arr) - 1  # Adjust the range here
    for i in range(EndingIndex):  # Adjust the range here
        a = Minimum(Arr, StartingIndex, EndingIndex)
        b = Arr[i]
        Arr[i] = Arr[a]
        Arr[a] = b
        StartingIndex = StartingIndex + 1
    return Arr

# Problem 5
def StringReverse(str, starting, ending):
    return str[starting:ending][::-1] 
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
# Problem 7
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
# Problem 9
def PalindromRecursive(str):
    Start=0
    if len(str)==0:
        return False
    elif(str[Start]!=str[-1]):
        return False
    else:
         Start+=1
         PalindromRecursive(str[Start:-1])
         return True
# Problem 10
def Sort10(Arr):
    Arr = Sort(Arr)
    positive = []
    negative = []
    sortedArray = []
    
    for i in range(len(Arr)):
        if Arr[i] >= 0:
            positive.append(Arr[i])
        else:
            negative.append(Arr[i])
    
    for i in range(max(len(positive), len(negative))):
        if i < len(negative):
            sortedArray.append(negative[i])
        if i < len(positive):
            sortedArray.append(positive[i])
    
    return sortedArray