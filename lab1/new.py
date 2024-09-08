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
            if i + 1 < len(arr) and arr[i] == arr[i+1]:  # Check to avoid IndexError
                newarr.append(i+1)
                break
    return newarr

# Problem 3
def Minimum(Arr,start,End):
    min = start
    for i in range(start,End+1):
        if(Arr[min]>Arr[i]):
            min=i
    return min

# Problem 4
def Sort(Arr):
    StartingIndex = 0
    EndingIndex = len(Arr) - 1  # Use dynamic EndingIndex based on list length
    for i in range(len(Arr)-1):
        a = Minimum(Arr, StartingIndex, EndingIndex)
        # Swap elements using temporary variable
        temp = Arr[i]
        Arr[i] = Arr[a]
        Arr[a] = temp
        StartingIndex = StartingIndex + 1
    return Arr

# Problem 5
def StringReverse(str,starting,ending):
    return str[starting:ending][::-1]  # Slicing with reverse step

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
    for i in range(len(matrix[0])):  # Fix to iterate over columns
        sum=0
        for j in range(len(matrix)):
            sum+=matrix[j][i]
        arr.append(sum)
    return arr

def RowWiseSum(matrix):
    arr=[]
    for i in range(len(matrix)):
        sum=0
        for j in range(len(matrix)):
            sum+=matrix[i][j]
        arr.append(sum)
    return arr

# Problem 8
def SortedMerge(Arr1, Arr2):
    StartingIndex = 0
    for i in range(len(Arr2)):
        Arr1.append(Arr2[i])
    for j in range(len(Arr1)):
        a = Minimum(Arr1, StartingIndex, len(Arr1)-1)
        # Swap elements using temporary variable
        temp = Arr1[j]
        Arr1[j] = Arr1[a]
        Arr1[a] = temp
        StartingIndex = StartingIndex + 1
    return Arr1

# Problem 9
# Problem 9
def PalindromRecursive(str):
    if len(str) <= 1:  # Base case: Single character or empty string is a palindrome
        return True
    elif str[0] != str[-1]:  # If the first and last characters don't match
        return False
    else:
        return PalindromRecursive(str[1:-1])  # Check the remaining substring


# Problem 10
def Sort10(Arr):
    Arr = Sort(Arr)  # Sort array first
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

