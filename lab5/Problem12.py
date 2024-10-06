numbers = [12, -7, 5, 64, -14, 25, -3, 42]

def remove_neg_num(number):
    positive_numbers = [num for num in number if num >= 0]
    return positive_numbers

def Maximum(numbers):
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum

def Minimum(numbers):
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum

def Average(numbers):
    sum = 0
    count = 0
    for num in numbers:
        sum += num
        count += 1
    return sum / count if count != 0 else 0

if __name__ == "__main__":
    print("List with negatives: " + str(numbers))
    numbers = remove_neg_num(numbers)
    print("List after removing negatives: " + str(numbers))

    maximum = Maximum(numbers)
    minimum = Minimum(numbers)
    print(f"Maximum value: {maximum}")
    print(f"Minimum value: {minimum}")

    average = Average(numbers)
    print(f"Average:{average}")