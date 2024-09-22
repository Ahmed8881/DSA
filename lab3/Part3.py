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


# PROBLEM 3   

def MatAddPartial(A, B, start, size):
    result = np.zeros((size, size))
    if not (start[0] + size > len(A) or start[1] + size > len(A[0]) or 
        start[0] + size > len(B) or start[1] + size > len(B[0])):
            for i in range(size):
                for j in range(size):
                    result[i][j] = A[start[0]+i][start[1]+j] + B[start[0]+i][start[1]+j]
    
            return result
 
#  PROBLEM 4       
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
    
#Problem 5
def MatMulRecursive(A, B):
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]
    mid = n // 2
    A11 = [[A[i][j] for j in range(mid)] for i in range(mid)]    # Dividing the matrices into 4 submatrices
    A12 = [[A[i][j] for j in range(mid, n)] for i in range(mid)]
    A21 = [[A[i][j] for j in range(mid)] for i in range(mid, n)]
    A22 = [[A[i][j] for j in range(mid, n)] for i in range(mid, n)]
    B11 = [[B[i][j] for j in range(mid)] for i in range(mid)]
    B12 = [[B[i][j] for j in range(mid, n)] for i in range(mid)]
    B21 = [[B[i][j] for j in range(mid)] for i in range(mid, n)]
    B22 = [[B[i][j] for j in range(mid, n)] for i in range(mid, n)]

    C11 = MatAdd(MatMulRecursive(A11, B11), MatMulRecursive(A12, B21))
    C12 = MatAdd(MatMulRecursive(A11, B12) , MatMulRecursive(A12, B22))
    C21 = MatAdd(MatMulRecursive(A21, B11) , MatMulRecursive(A22, B21))
    C22 = MatAdd(MatMulRecursive(A21, B12) , MatMulRecursive(A22, B22))

    C = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(mid):
        for j in range(mid):
            C[i][j] = C11[i][j]
            C[i][j + mid] = C12[i][j]
            C[i + mid][j] = C21[i][j]
            C[i + mid][j + mid] = C22[i][j]
    return C
def subtract_matrices(A, B):
    n = len(A)
    C = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] - B[i][j]
    return C
# Problem 6
def strassen(A, B):
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]
    mid = n // 2
    A11 = [[A[i][j] for j in range(mid)] for i in range(mid)]    # Dividing the matrices into 4 submatrices
    A12 = [[A[i][j] for j in range(mid, n)] for i in range(mid)]
    A21 = [[A[i][j] for j in range(mid)] for i in range(mid, n)]
    A22 = [[A[i][j] for j in range(mid, n)] for i in range(mid, n)]
    B11 = [[B[i][j] for j in range(mid)] for i in range(mid)]
    B12 = [[B[i][j] for j in range(mid, n)] for i in range(mid)]
    B21 = [[B[i][j] for j in range(mid)] for i in range(mid, n)]
    B22 = [[B[i][j] for j in range(mid, n)] for i in range(mid, n)]
    
    M1 = strassen(MatAdd(A11, A22), MatAdd(B11, B22))   #Recusive calls
    M2 = strassen(MatAdd(A21, A22), B11)
    M3 = strassen(A11, subtract_matrices(B12, B22))
    M4 = strassen(A22, subtract_matrices(B21, B11))
    M5 = strassen(MatAdd(A11, A12), B22)
    M6 = strassen(subtract_matrices(A21, A11), MatAdd(B11, B12))
    M7 = strassen(subtract_matrices(A12, A22), MatAdd(B21, B22))

    C11 = MatAdd(subtract_matrices(MatAdd(M1, M4), M5), M7)
    C12 = MatAdd(M3, M5)
    C21 = MatAdd(M2, M4)
    C22 = MatAdd(subtract_matrices(MatAdd(M1, M3), M2), M6)

    C = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(mid):
        for j in range(mid):
            C[i][j] = C11[i][j]
            C[i][j + mid] = C12[i][j]
            C[i + mid][j] = C21[i][j]
            C[i + mid][j + mid] = C22[i][j]
    return C

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
# A=[[2,3],[4,5]]
# B=[[1],[3]]
# print(MatMul(A,B))
# print(MatMulRecursive(A,B))