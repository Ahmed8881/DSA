import unittest
import funcs  # Assuming the functions are in a file named funcs.py


class TestFunctions(unittest.TestCase):

    # Test Problem 1: SearchIndex
    def test_search_index_single_occurrence(self):
        self.assertEqual(funcs.SearchIndex([1, 2, 3, 4, 5], 3), [2])

    def test_search_index_multiple_occurrences(self):
        self.assertEqual(funcs.SearchIndex([1, 2, 3, 3, 5], 3), [2, 3])

    def test_search_index_no_occurrence(self):
        self.assertEqual(funcs.SearchIndex([1, 2, 3, 4, 5], 6), [])

    # Test Problem 2: SearchIndex (modified version)
    def test_search_index_adjacent_duplicates(self):
        self.assertEqual(funcs.SearchIndex([1, 2, 3, 3, 5], 3), [2, 3])

    # Test Problem 3: Minimum
    def test_minimum_basic(self):
        self.assertEqual(funcs.Minimum([3, 1, 4, 1, 5], 0, 4), 1)

    def test_minimum_subarray(self):
        self.assertEqual(funcs.Minimum([3, 1, 4, 1, 5], 1, 3), 1)

    # Test Problem 4: Sort
    def test_sort_basic(self):
        self.assertEqual(funcs.Sort([3, 1, 4, 1, 5]), [1, 1, 3, 4, 5])

    def test_sort_reverse(self):
        self.assertEqual(funcs.Sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    # Test Problem 5: StringReverse
    def test_string_reverse_basic(self):
        self.assertEqual(funcs.StringReverse("hello", 0, 5), "olleh")

    # Test Problem 6: SumIteratice and SumRecursive
    def test_sum_iterative(self):
        self.assertEqual(funcs.SumIteratice(12345), 15)

    def test_sum_recursive(self):
        self.assertEqual(funcs.SumRecursive(12345), 15)

    # Test Problem 7: ColumnWiseSum and RowWiseSum
    def test_column_wise_sum(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(funcs.ColumnWiseSum(matrix), [12, 15, 18])

    def test_row_wise_sum(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(funcs.RowWiseSum(matrix), [6, 15, 24])

    # Test Problem 8: SortedMerge
    def test_sorted_merge(self):
        self.assertEqual(funcs.SortedMerge([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])

    # Test Problem 9: PalindromRecursive
    def test_palindrom_recursive_palindrome(self):
        self.assertTrue(funcs.PalindromRecursive("radar"))

    def test_palindrom_recursive_not_palindrome(self):
        self.assertFalse(funcs.PalindromRecursive("hello"))

    # Test Problem 10: Sort10
    def test_sort10_basic(self):
        self.assertEqual(funcs.Sort10([10, -1, 9, 20, -3, -8, 22, 9, 7]),
                         [-8, 7, -3, 9, -1, 9, 10, 20, 22])


if __name__ == "__main__":
    unittest.main()
