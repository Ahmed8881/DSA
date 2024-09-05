def SumIteratice(number):
    sum=0
    while(number>0):
        sum+=number%10
        number=number//10
    return sum

def SumRecursive(number):
    if number==0:
        return 0
    else:
        return number%10+SumRecursive(number//10)
      
sum1=SumIteratice(111111)
print(sum1)
sum2=SumRecursive(12)
print(sum2)