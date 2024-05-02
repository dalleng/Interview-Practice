#!/usr/bin/env python3
import unittest


def array_left_rotation(a, n, k):
    rotations = k % n
    return a[rotations:] + a[:rotations]


class ArrayLRTest(unittest.TestCase):
    def test_sample(self):
        a = list(range(1, 6))
        self.assertEqual(array_left_rotation(a, len(a), 4), [5, 1, 2, 3, 4])

    def test_single_element(self):
        a = [1]
        self.assertEqual(array_left_rotation(a, len(a), 1), [1])

    def test_rotations_bigger_than_length_of_array(self):
        a = list(range(1, 6))
        self.assertEqual(array_left_rotation(a, len(a), 6), [2, 3, 4, 5, 1])

    def test_move_every_item(self):
        a = list(range(1, 6))
        self.assertEqual(array_left_rotation(a, len(a), 5), a)


if __name__ == "__main__":
    unittest.main()
