def printMatrix(A,starting_index,rows,columns):
    list1=[]
    for i in range(starting_index[0],rows):
        for j in range(starting_index[1],columns):
            list1.append(A[i][j])
    return list1



# driver code
A=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
# Starting index is a tuple
starting_index = (0, 3)
rows=3
columns=4
print(printMatrix(A,starting_index,rows,columns))
