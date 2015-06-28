import unittest
from random import randint


def insertion_sort(l):
    for i in range(1, len(l)):
        value = l[i]
        hole = i
        while value < l[hole - 1] and hole > 0:
            l[hole] = l[hole - 1]
            hole -= 1
        l[hole] = value


class SortTest(unittest.TestCase):
    def test_empty(self):
        l = []
        insertion_sort(l)
        self.assertEquals(l, sorted([]))

    def test_descending(self):
        l = range(10, 0, -1)
        insertion_sort(l)
        self.assertEquals(l, range(1, 11))

    def test_randon(self):
        length = randint(1, 100)
        l = [randint(1, 100) for _ in range(length)]
        print l
        lcopy = l[:]
        insertion_sort(l)
        print l
        self.assertEquals(l, sorted(lcopy))


if __name__ == '__main__':
    unittest.main()
