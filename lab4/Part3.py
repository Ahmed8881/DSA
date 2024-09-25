
def Max(input):
    for i in range(0, len(input)-1):
        if(input[i]>input[i+1]):
            max=input[i]
    return max

def CountingSort(input):
    max_val = Max(input)
    count = [0] * (max_val + 1)
    for i in input:
        count[i] += 1
    output = []
    for i in range(len(count)):
        output.extend ([i] * count[i])
    return output

def BucketSort(arr,n):
    bucket = []
    for i in range(n):
        bucket.append([])
    for i in range(n):
        index = int(n*arr[i])
        bucket[index].append(arr[i])
    for i in range(n):
        bucket[i] = CountingSort(bucket[i])
    k = 0
    for i in range(n):
        for j in range(len(bucket[i])):
            arr[k] = bucket[i][j]
            k += 1
    return arr


A=[4,6,5,3,7,1]
print(CountingSort(A))
# print(BucketSort(A,len(A)))
        


