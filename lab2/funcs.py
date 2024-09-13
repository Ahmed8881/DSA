
from random import randint
def RandomArray(size):
   return [randint(-15000,15000) for _ in range(size)]

def isSorted(array,Start,End):
    return all(array[i] <= array[i+1] for i in range(Start,End-1))

