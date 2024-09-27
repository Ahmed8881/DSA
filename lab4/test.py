def comb_sort(arr):
    n = len(arr)
    gap = n
    shrink = 1.3
    is_sorted = False

    while gap > 1 or not is_sorted:
        gap = int(gap / shrink)
        if gap < 1:
            gap = 1

        is_sorted = True

        for i in range(n - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                is_sorted = False

    return arr  # Return the sorted array

def test_comb_sort():
    test_cases = [
        # Standard cases
        ([3, 1, 4, 1, 5, 9, 2, 6, 5], [1, 1, 2, 3, 4, 5, 5, 6, 9]),
        ([5, 3, 8, 4, 2], [2, 3, 4, 5, 8]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([7, 7, 7, 7], [7, 7, 7, 7]),
        ([42], [42]),
        ([], []),
        ([56, 12, 99, 34, 76, 1], [1, 12, 34, 56, 76, 99]),
        ([1000, 2500, 300, 100, 10], [10, 100, 300, 1000, 2500]),
        ([123, 45, 6, 7890], [6, 45, 123, 7890]),
        
        # Edge cases
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),  # Already sorted
        ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),  # Reverse order
        ([0, -1, -2, -3, -4], [-4, -3, -2, -1, 0]),  # Negative numbers
        ([1, 2, 3, -1, -2], [-2, -1, 1, 2, 3]),  # Mixed positive and negative
        ([5, 5, 5, 5, 5], [5, 5, 5, 5, 5]),  # All elements the same

        # Random order
        ([34, 2, 23, 89, 2, 14, 55], [2, 2, 14, 23, 34, 55, 89]),
        ([101, 34, 56, 78, 43, 12, 67], [12, 34, 43, 56, 67, 78, 101]),
        ([1000, 100, 10, 1, 10000, 999], [1, 10, 100, 999, 1000, 10000]),
        ([5, 10, 3, 8, 6, 2], [2, 3, 5, 6, 8, 10]),
        ([15, 3, 9, 27, 2], [2, 3, 9, 15, 27]),

        # Large numbers
        ([1000000, 500000, 2000000, 1500000], [500000, 1000000, 1500000, 2000000]),
        ([987654321, 123456789, 234567890], [123456789, 234567890, 987654321]),

        # Mixed types (integers and floats)
        ([3.14, 2, 1.5, 4, 0.5], [0.5, 1.5, 2, 3.14, 4]),

        # Randomized large array
        ([5, 1, 4, 2, 8, 6, 7, 3, 9, 0], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
        ([12, 11, 10, 10, 12, 11], [10, 10, 11, 11, 12, 12]),
        
        # More edge cases
        ([2, 1], [1, 2]),  # Two elements
        ([1], [1]),  # Single element
        ([-1, 0, 1], [-1, 0, 1])  # Negative, zero, and positive
    ]
    
    for i, (input_data, expected) in enumerate(test_cases):
        result = comb_sort(input_data.copy())  # Sort a copy of the input
        assert result == expected, f"Test case {i + 1} failed: expected {expected}, got {result}"
        print(f"Test case {i + 1} passed!")

# Run the test cases
if __name__ == "__main__":
    test_comb_sort()

