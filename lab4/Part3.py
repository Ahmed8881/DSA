
def Max(input):
    max_val = input[0]
    for i in range(1, len(input)):
        if input[i] > max_val:
            max_val = input[i]
    return max_val

def CountingSort(input):
    min_val = min(input)
    max_val = max(input)
    range_of_elements = max_val - min_val + 1
    count = [0] * range_of_elements
    output = [0] * len(input)

    for i in range(len(input)):
        count[input[i] - min_val] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for i in range(len(input) - 1, -1, -1):
        output[count[input[i] - min_val] - 1] = input[i]
        count[input[i] - min_val] -= 1

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


A=[-5, -10, 0, -3, 8, 5,  -1, 10] 
print(CountingSort(A))
# print(BucketSort(A,len(A)))
        


      