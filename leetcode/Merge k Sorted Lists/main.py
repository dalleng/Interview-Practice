import time
import unittest
import heapq
from longlist import longlist
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        s = '{}'.format(self.val)
        n = self.next
        while n:
            s += ' -> {}'.format(n.val)
            n = n.next
        return s

    def __eq__(self, other):
        return str(self) == str(other)


def buildLinkedList(iterable):
    root = ListNode(iterable[0])
    tail = root
    for val in iterable[1:]:
        node = ListNode(val)
        tail.next = node
        tail = node
    return root


class Solution:
    # @param {ListNode[]} lists
    # @return {ListNode}
    """
    Slow solution
    def mergeKLists(self, lists):
        newList = ListNode(None)
        tail = newList
        minIndex = None
        emptyLists = 0
        linkedLists = len(lists)

        while emptyLists != linkedLists:
            emptyLists = 0

            for i, head in enumerate(lists):
                if head is None:
                    emptyLists += 1
                elif minIndex is None or head.val < lists[minIndex].val:
                    minIndex = i

            if minIndex is not None:
                tail.next = lists[minIndex]
                tail = tail.next
                lists[minIndex] = lists[minIndex].next
                minIndex = None

        tail.next = None
        return newList.next
    """

    # Same approach, slightly simplified. Added on 28/July/2021
    def mergeKLists2(self, lists: List[ListNode]) -> ListNode:
        merged = []

        for ll in lists:
            current = ll
            while current:
                heapq.heappush(merged, current.val)
                current = current.next

        head = None
        previous = None

        while merged:
            val = heapq.heappop(merged)
            node = ListNode(val=val)

            if head is None:
                head = node
            else:
                previous.next = node
                previous = node

            previous = node

        return head

    def mergeKLists(self, lists):
        heap = []

        for head in lists:
            while head is not None:
                heapq.heappush(heap, (head.val, head))
                head = head.next

        sorted_list = None
        tail = None

        while heap:
            _, node = heapq.heappop(heap)
            if sorted_list is None:
                sorted_list = node
                tail = node
            else:
                tail.next = node
                tail = node
                tail.next = None

        return sorted_list


class TestMerge(unittest.TestCase):
    s = Solution()

    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        print "%f seconds" % (t,)

    def test_merge_two(self):
        # 2 -> 4 -> 6 -> 8
        l1 = buildLinkedList(range(2, 10, 2))

        # 1 -> 3 -> 5 -> 9
        l2 = buildLinkedList(range(1, 10, 2))

        lists = [l1, l2]
        root = self.s.mergeKLists(lists)
        self.assertEquals(root, buildLinkedList(range(1, 10)))

    def test_single_element(self):
        l = buildLinkedList((1,))
        lists = [l]
        root = self.s.mergeKLists(lists)
        self.assertEquals(str(root), '1')

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
        self.assertEquals(root, buildLinkedList(sorted(l1 + l2 + l3 + l4)))

    def test_very_large_list(self):
        flatten = lambda l: reduce(lambda x, y: x + y, l, [])
        flattened = flatten(longlist)
        lists = [buildLinkedList(l) for l in longlist]
        root = self.s.mergeKLists(lists)
        self.assertEquals(root, buildLinkedList(sorted(flattened)))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMerge)
    unittest.TextTestRunner(verbosity=2).run(suite)
