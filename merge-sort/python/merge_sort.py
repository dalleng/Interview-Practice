import unittest
from random import randint


def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    else:
        middle = len(nums) / 2
        first_half = nums[:middle]
        second_half = nums[middle:]
        return merge(merge_sort(first_half), merge_sort(second_half))


def merge(a, b):
    pos_a = 0
    pos_b = 0
    merged = []
    len_a = len(a)
    len_b = len(b)

    while pos_a < len_a or pos_b < len_b:
        if pos_a == len_a:
            merged.append(b[pos_b])
            pos_b += 1
        elif pos_b == len_b:
            merged.append(a[pos_a])
            pos_a += 1
        elif a[pos_a] < b[pos_b]:
            merged.append(a[pos_a])
            pos_a += 1
        else:
            merged.append(b[pos_b])
            pos_b += 1

    return merged


class MergeTest(unittest.TestCase):
    def test_same_length(self):
        self.assertEquals(merge([1, 3, 5], [2, 4, 6]), range(1, 7))

    def test_different_length(self):
        self.assertEquals(merge([1], [2, 3, 4]), range(1, 5))

    def test_one_empty(self):
        self.assertEquals(merge([], [2, 3, 4]), range(2, 5))


class MergeSortTest(unittest.TestCase):
    def test_empty(self):
        self.assertEquals(merge_sort([]), [])

    def test_reverse(self):
        self.assertEquals(merge_sort(range(5, 0, -1)), range(1, 6))

    def test_random(self):
        n = 100
        [randint(1, 100) for _ in range(n)]

if __name__ == '__main__':
    unittest.main()
