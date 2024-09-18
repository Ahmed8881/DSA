import csv
from random import randint
import random

import numpy as np

#Function to Find Factorial
def factorial(n):
    if(n==0):
        return 1
    else:
        return n* factorial(n-1)

#Function to Generate Random Numbers
def RandomArray(size):
   return [randint(-15000, 15000) for i in range(size)]

#Function to read File
def ReadFile(filename):
    f = open(file = filename , mode = 'r')
    lines = f.read()
    numbers = []
    arr = lines.split()
    for s in arr:
        num = int(s)
        numbers.append(num)
    return numbers

#Function to Merge array
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


#Function to Write in tabular form
def WriteFile(filename, array):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        for row in array:
            writer.writerow(row)
 
            
#Function to Write in File
def WriteFiles(filename, arr):
    f = open(file = filename , mode = 'w')
    for i in arr:
        f.write(str(i) + "\n")           


#Function to Read words from file
def ReadWords(filename):
    f = open(file = filename , mode = 'r')
    lines = f.read()
    words = []
    arr = lines.split()
    for i in arr:
        words.append(i)
    return words 

 
#Function to Shuffle Array
# def ShuffleArray(array, start, end):
#     for i in range(end-1, start, -1):
#         j = randint(start, i)
#         array[i], array[j] = array[j], array[i]
#     return array
def ShuffleArray(arr,start,end):
    return (random.shuffle(arr))