import unittest


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        s = "{}".format(self.val)
        n = self.next
        while n:
            s += " -> {}".format(n.val)
            n = n.next
        return s

    __repr__ = __str__

    def __eq__(self, other):
        return str(self) == str(other)


class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        if head is None:
            return None

        while head and head.val == val:
            head = head.next

        current = head
        previous = head

        while current:
            if current == previous:
                current = current.next
            elif current.val == val:
                current = current.next
                previous.next = current
            else:
                previous = current
                current = current.next

        return head


def buildLinkedList(iterable):
    root = ListNode(iterable[0])
    tail = root
    for val in iterable[1:]:
        node = ListNode(val)
        tail.next = node
        tail = node
    return root


class RemoveElementsTest(unittest.TestCase):
    s = Solution()

    def test_val_front(self):
        l1 = buildLinkedList("66234")
        l2 = buildLinkedList("234")
        self.assertEquals(self.s.removeElements(l1, "6"), l2)

    def test_val_middle(self):
        l1 = buildLinkedList("26634")
        l2 = buildLinkedList("234")
        self.assertEquals(self.s.removeElements(l1, "6"), l2)

    def test_val_end(self):
        l1 = buildLinkedList("23466")
        l2 = buildLinkedList("234")
        self.assertEquals(self.s.removeElements(l1, "6"), l2)

    def test_only_val(self):
        l1 = buildLinkedList("66")
        r = self.s.removeElements(l1, "6")
        self.assertEquals(r, None)


if __name__ == "__main__":
    unittest.main()
