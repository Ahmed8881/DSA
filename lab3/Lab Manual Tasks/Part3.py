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
def MatSubtract(A, B):
    C = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] - B[i][j])
        C.append(row)
    return C
def Adjust_dimension(matrix, size):
    padded = np.zeros((size, size), dtype=int)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            padded[i][j] = matrix[i][j]
    return padded

def next_power_of_2(x):
    return 1 if x == 0 else 2**(x - 1).bit_length()

def MatMulStrassen(A, B):
    n = len(A)
    m = next_power_of_2(n)
    A = Adjust_dimension(A, m)
    B = Adjust_dimension(B, m)

    if m == 1:
        return [[A[0][0] * B[0][0]]]

    mid = m // 2

    # Dividing the matrices into 4 submatrices
    A11 = [[A[i][j] for j in range(mid)] for i in range(mid)]
    A12 = [[A[i][j] for j in range(mid, m)] for i in range(mid)]
    A21 = [[A[i][j] for j in range(mid)] for i in range(mid, m)]
    A22 = [[A[i][j] for j in range(mid, m)] for i in range(mid, m)]
    B11 = [[B[i][j] for j in range(mid)] for i in range(mid)]
    B12 = [[B[i][j] for j in range(mid, m)] for i in range(mid)]
    B21 = [[B[i][j] for j in range(mid)] for i in range(mid, m)]
    B22 = [[B[i][j] for j in range(mid, m)] for i in range(mid, m)]

    # Recursive calls
    P1 = MatMulStrassen(MatAdd(A11, A22), MatAdd(B11, B22))
    P2 = MatMulStrassen(MatAdd(A21, A22), B11)
    P3 = MatMulStrassen(A11, MatSubtract(B12, B22))
    P4 = MatMulStrassen(A22, MatSubtract(B21, B11))
    P5 = MatMulStrassen(MatAdd(A11, A12), B22)
    P6 = MatMulStrassen(MatSubtract(A21, A11), MatAdd(B11, B12))
    P7 = MatMulStrassen(MatSubtract(A12, A22), MatAdd(B21, B22))

    C11 = MatAdd(MatSubtract(MatAdd(P1, P4), P5), P7)
    C12 = MatAdd(P3, P5)
    C21 = MatAdd(P2, P4)
    C22 = MatAdd(MatSubtract(MatAdd(P1, P3), P2), P6)

    C = [[0 for _ in range(m)] for _ in range(m)]

    for i in range(mid):
        for j in range(mid):
            C[i][j] = C11[i][j]
            C[i][j + mid] = C12[i][j]
            C[i + mid][j] = C21[i][j]
            C[i + mid][j + mid] = C22[i][j]

    return [row[:n] for row in C[:n]]

if __name__ == "__main__":
    A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    B = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    print("Matrix A:")
    for i in A:
        print(i)
    print("\nMatrix Addition:")
    printMatrix(MatAdd(A, B), [0, 0], 4, 4)
    print("\nMatrix Multiplication:")
    printMatrix(MatMul(A, B), [0, 0], 4, 4)
    print("\nMatrix Multiplication Recursive:")
    printMatrix(MatMulRecursive(A, B), [0, 0], 4, 4)
    print("\nMatrix Multiplication MatMulStrassen:")
    printMatrix(MatMulStrassen(A, B), [0, 0], 4, 4)
    print("\nMatrix Addition Partial:")
    print(MatAddPartial(A, B, [1, 1], 2))