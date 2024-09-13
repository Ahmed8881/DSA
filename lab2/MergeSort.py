import funcs
import time

def MergeSort(array, start, end):
    if start >= end:
        return array

    mid = (start + end) // 2
    left = MergeSort(array, start, mid)
    right = MergeSort(array, mid, end)

    i = 0
    j = 0
    k = start

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1

    return array

if __name__ == "__main__":
    n = 16
    array = funcs.RandomArray(n)
    start_time = time.perf_counter()
    new_array = MergeSort(array, 0, n)
    end_time = time.perf_counter()
    print(funcs.isSorted(new_array, 0, n))
    run_time = end_time - start_time
    print("Run time of MergeSort at", n, "is", run_time, "seconds")
