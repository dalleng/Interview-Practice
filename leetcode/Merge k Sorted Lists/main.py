import time
import unittest
import heapq
from longlist import longlist
from typing import List, Optional
import functools


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        s = '{}'.format(self.val)
        n = self.next
        while n:
            s += ' -> {}'.format(n.val)
            n = n.next
        return s


def buildLinkedList(iterable):
    root = ListNode(iterable[0])
    tail = root
    for val in iterable[1:]:
        node = ListNode(val)
        tail.next = node
        tail = node
    return root


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        merged = []
        result_root = None

        for root in lists:
            current = root
            while current:
                heapq.heappush(merged, current.val)
                current = current.next

        if merged:
            result_root = ListNode(val=heapq.heappop(merged))

        current = result_root
        while merged:
            current.next = ListNode(val=heapq.heappop(merged))
            current = current.next

        return result_root


class TestMerge(unittest.TestCase):
    s = Solution()

    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        print("%f seconds" % (t,))

    def test_merge_two(self):
        # 2 -> 4 -> 6 -> 8
        l1 = buildLinkedList(range(2, 10, 2))

        # 1 -> 3 -> 5 -> 9
        l2 = buildLinkedList(range(1, 10, 2))

        lists = [l1, l2]
        root = self.s.mergeKLists(lists)
        self.assertEqual(str(root), str(buildLinkedList(range(1, 10))))

    def test_single_element(self):
        l = buildLinkedList((1,))
        lists = [l]
        root = self.s.mergeKLists(lists)
        self.assertEqual(str(root), '1')

    def test_merge_four(self):
        l1 = [1, 15, 200]
        l2 = [2, 5, 9]
        l3 = [2, 15, 29]
        l4 = [-2, 0, 5, 9, 27, 44, 116, 300]
        lists = [
            buildLinkedList(l1),
            buildLinkedList(l2),
            buildLinkedList(l3),
            buildLinkedList(l4),
        ]
        root = self.s.mergeKLists(lists)
        self.assertEquals(str(root), str(buildLinkedList(sorted(l1 + l2 + l3 + l4))))

    def test_very_large_list(self):
        flatten = lambda l: functools.reduce(lambda x, y: x + y, l, [])  # noqa
        flattened = flatten(longlist)
        lists = [buildLinkedList(ll) for ll in longlist]
        root = self.s.mergeKLists(lists)
        self.assertEquals(str(root), str(buildLinkedList(sorted(flattened))))


if __name__ == '__main__':
    unittest.main()
