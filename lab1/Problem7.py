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
       
   