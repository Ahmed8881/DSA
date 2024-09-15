
from random import randint
def RandomArray(size):
   return [randint(-15000,15000) for _ in range(size)]

def isSorted(array,Start,End):
    return all(array[i] <= array[i+1] for i in range(Start,End-1))

def Merge(array, p, q, r):
    
    Left = q - p + 1 
    Right = r - q
    
    L = [0] * Left   
    R = [0] * Right
    
    for i in range(0, Left):
        L[i] = array[p + i]

    for j in range(0, Right):
        R[j] = array[q + 1 + j]
    
    i = 0
    j = 0
    k = p
    
    while i < Left  and j < Right:
        if L[i] <= R[j]:
            array[k] = L[i]
            i+=1
        else:
            array[k] = R[j]
            j+=1
        k+=1
    
    while i<Left:
        array[k] = L[i]
        i+=1
        k+=1

    while j<Right:
        array[k] = R[j]
        j+=1
        k+=1
