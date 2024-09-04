# print("Hello to Data Structure and Algorithms Course")
# No compulsory library is required for 
# a=5
# print("The value of a is ",a)
# a = input ("Enter the value:") #a is string 
#conversion of string to int data type 
# b = int(a) 
# print ("Entered value is:" ,b) 
 
#We need to convert int type variable to string. Because in python concatenation of 
# int and string type variables is not possible without conversion.
# Declare 1-D array
# array=[]
# array=[1,2,3,4,5]
# print(array)
# # Declare 2-D array
# array2D=[[1,2,3],[4,5,6],[7,8,9]]
# print(array2D)
# array= 0*20
# array = [0] * 10
# print(array)
# array1 = [[0 for x in range(4)] for y in range(3)]
# print(array1)
# newarray=[[1 for x in range (10)],[2 for x in range (10)]]
# print(newarray)
#we can perform the same task more easily using numpy library 
# TODO—add numpy code for zeros
# import numpy as np
# array = np.zeros(10)
# print(array)
import random
array=[]
min=0
max=20
# for i in range(10):
#     num=random.randint(min,max)
#     array.append(num)
# print(array) 
  #Traverse in forward direction using 
# for loop 
# str = ["apple", "banana", "cherry"] 
# for x in range(len(str)): 
#     print(str[x]) 
 
array = [32, 1, 9, 31, 12, 22] 
  
# Reverse by using a slice 
# slice (start, end, step) 
# print(array[::-1]) 
#Traverse in backward direction using reverse 
# method 

# array.reverse() 
# print(array) 
  
#Traverse through an array using for loop 
# for i in range(len(array)-1, -1, -1): 
#  print(array[i])
def display(arr): 
    for i in arr: 
        print(i) 
 
array = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
display(array) 