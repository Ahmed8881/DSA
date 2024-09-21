import numpy as np


# PROBLEM 1
def printMatrix(A, starting_index, rows, columns):    
    for i in range(starting_index[0], rows):
        if not (0 <= starting_index[0] < rows and 0 <= starting_index[1] < columns):
            break
        for j in range(starting_index[1], columns):
            print(A[i][j], end=" ")
        print()
        
# Problem 2
def MatAdd(A, B):
    Sum = []
    if len(A) == len(B) and len(A[0]) == len(B[0]):
        for i in range(len(A)):
            row = []
            for j in range(len(A[0])):
                row.append(A[i][j] + B[i][j])
            Sum.append(row)
    return Sum
       
def MatAddPartial(A, B, start, size):
    result = np.zeros((size, size))
    if not (start[0] + size > len(A) or start[1] + size > len(A[0]) or 
        start[0] + size > len(B) or start[1] + size > len(B[0])):
            for i in range(size):
                for j in range(size):
                    result[i][j] = A[start[0]+i][start[1]+j] + B[start[0]+i][start[1]+j]
    
            return result
        
def MatMul(A, B):
    if len(A[0]) == len(B):
        result = []
        for i in range(len(A)):
            row = []
            for j in range(len(B[0])):
                sum = 0
                for k in range(len(B)):
                    sum += A[i][k] * B[k][j]
                row.append(sum)
            result.append(row)
        return result
# if __name__ == "__main__":
    # Problem 1
    # A=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    # printMatrix(A,[1,2],4,4)
    #Problem 2
#    A=[[1,2,3],[4,5,6],[7,8,9]]
#    B=[[9,8,7],[6,5,4],[3,2,1]]
#    print(MatAddPartial(A,B,[1,0],2))
# A = [
#     [1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 10],
#     [11, 12, 13, 14, 15],
#     [16, 17, 18, 19, 20],
#     [21, 22, 23, 24, 25]
# ]

# B = [
#     [1, 1, 1, 1, 1],
#     [2, 2, 2, 2, 2],
#     [3, 3, 3, 3, 3],
#     [4, 4, 4, 4, 4],
#     [5, 5, 5, 5, 5]
# ]

# start = (2, 3)
# size = 2

# result = MatAddPartial(A, B, start, size)
# print(result)

# Driver fir mul
A=[[2,3],[4,5]]
B=[[1],[3]]
print(MatMul(A,B))  