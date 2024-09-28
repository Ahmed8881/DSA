from random import randint

def QuickSort(A, p, r):
    if p < r:
        q = Partition(A, p, r)
        QuickSort(A, p, q-1)
        QuickSort(A, q+1, r)
    return A

def Partition(A, p, r):
    # Choose the last element as the pivot
    x = A[r]
    i = p - 1
    for j in range(p, r):
        # If the current element is smaller than or equal to the pivot
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i + 1

# A = [2, 8, 7, 1, 3, 5, 6, 4]
# QuickSort(A, 0, len(A) - 1)
# print(A)

def RandomArray(size):
   return [randint(-15000, 15000) for i in range(size)]

#Function to Write in File
def WriteFiles(filename, arr):
    f = open(filename, 'w')
    f = open(file = filename , mode = 'w')
    for i in arr:
        f.write(str(i) + "\n")     
        

if __name__=="__main__":
    n = 30000
    array = RandomArray(n)
    new_array = QuickSort(array, 0, n-1)
    WriteFiles("SortedQuickSort.csv", new_array)
    
    
   