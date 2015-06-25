import unittest


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

    __repr__ = __str__

    def __eq__(self, other):
        return str(self) == str(other)


class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        head = None
        node = None
        ptr1 = l1
        ptr2 = l2
        carry = 0

        while ptr1 or ptr2:
            op1 = ptr1.val if ptr1 else 0
            op2 = ptr2.val if ptr2 else 0
            sum = op1 + op2 + carry
            carry = 0

            if sum >= 10:
                carry = int(str(sum)[0])
                sum = int(str(sum)[1])

            if head is None:
                head = ListNode(sum)
                node = head
            else:
                node.next = ListNode(sum)
                node = node.next

            ptr1 = ptr1.next if ptr1 else ptr1
            ptr2 = ptr2.next if ptr2 else ptr2

        if carry:
            node.next = ListNode(carry)

        return head


def buildLinkedList(iterable):
    root = ListNode(iterable[0])
    tail = root
    for val in iterable[1:]:
        node = ListNode(val)
        tail.next = node
        tail = node
    return root


class addTwoNumbersTest(unittest.TestCase):
    def test_example(self):
        l1 = buildLinkedList([2, 4, 3])
        l2 = buildLinkedList([5, 6, 4])
        self.assertEquals(Solution().addTwoNumbers(l1, l2),
                          buildLinkedList([7, 0, 8]))

    def test_l2_less_digits(self):
        l1 = buildLinkedList([2, 4, 3])
        l2 = buildLinkedList([6, 4])
        self.assertEquals(Solution().addTwoNumbers(l1, l2),
                          buildLinkedList([8, 8, 3]))

    def test_l1_less_digits(self):
        l1 = buildLinkedList([2, 4, 3])
        l2 = buildLinkedList([9, 9])
        self.assertEquals(Solution().addTwoNumbers(l1, l2),
                          buildLinkedList([1, 4, 4]))

    def test_l1_none(self):
        l1 = None
        l2 = buildLinkedList([9, 9])
        self.assertEquals(Solution().addTwoNumbers(l1, l2),
                          buildLinkedList([9, 9]))

    def test_one_more_carry(self):
        l1 = ListNode(5)
        l2 = ListNode(5)
        self.assertEquals(Solution().addTwoNumbers(l1, l2),
                          buildLinkedList([0, 1]))

if __name__ == '__main__':
    unittest.main()
