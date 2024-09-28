
def Max(input):
    max_val = input[0]
    for i in range(1, len(input)):
        if input[i] > max_val:
            max_val = input[i]
    return max_val

def InsertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
# Sorting Algorithems
def CountingSort(input):
    min_val = min(input)
    max_val = max(input)
    range_of_elements = int(max_val * 1000) - int(min_val * 1000) + 1
    count = [0] * range_of_elements
    output = [0] * len(input)

    for i in range(len(input)):
        count[int(input[i] * 1000) - int(min_val * 1000)] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for i in range(len(input) - 1, -1, -1):
        output[count[int(input[i] * 1000) - int(min_val * 1000)] - 1] = input[i]
        count[int(input[i] * 1000) - int(min_val * 1000)] -= 1

    return output

def bucketSort(arr, n):
    # Create n empty buckets
    buckets = [[] for _ in range(n)]
    sorted_list = []

    # Put array elements in different buckets
    min_val = arr[0]
    max_val = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < min_val:
            min_val = arr[i]
        if arr[i] > max_val:
            max_val = arr[i]

    for i in range(len(arr)):
        index = int(n * (arr[i] - min_val) / (max_val - min_val + 1))
        buckets[index].append(arr[i])

    # Sort individual buckets using insertion sort
    for i in range(n):
        buckets[i] = InsertionSort(buckets[i])

    # Concatenate all sorted buckets
    for bucket in buckets:
        sorted_list.extend(bucket)

    return sorted_list

def countingSortForRadix(arr, digit_place):
    buckets = [[] for _ in range(10)]

    for number in arr:
        index = abs(number) // digit_place % 10
        buckets[index].append(number)

    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(bucket)

    return sorted_array


def RadixSort(arr):
    if len(arr) == 0:
        return arr

    # Separate positive and negative numbers
    positive_numbers = [num for num in arr if num >= 0]
    negative_numbers = [-num for num in arr if num < 0]

    # Sort positive numbers
    if positive_numbers:
        max_value = max(positive_numbers)
        digit_place = 1
        while max_value // digit_place > 0:
            positive_numbers = countingSortForRadix(positive_numbers, digit_place)
            digit_place *= 10

    # Sort negative numbers
    if negative_numbers:
        max_value = max(negative_numbers)
        digit_place = 1
        while max_value // digit_place > 0:
            negative_numbers = countingSortForRadix(negative_numbers, digit_place)
            digit_place *= 10
        negative_numbers = [-num for num in reversed(negative_numbers)]

    # Combine sorted positive and negative numbers
    return negative_numbers + positive_numbers

A=[-5, -10, 0, -3, 8, 5,  -1, 10] 
B=[110, 45, 65,50, 90,   
602, 24, 2, 66]  
C=[0.897, 0.565, 0.656,  
0.1234, 0.665, 0.3434] 
# print(CountingSort(A))
# print(CountingSort(B))
# print(CountingSort(C))
# print(bucketSort(A,len(A)))
# print(bucketSort(B,len(B)))
# print(bucketSort(C,len(C)))
# print(RadixSort(A))
# print(RadixSort(B))
# print(RadixSort(C))
        


      