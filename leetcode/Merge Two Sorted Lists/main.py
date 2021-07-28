# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        c1 = l1
        c2 = l2
        head = None
        previous = None
        while c1 or c2:
            if c1 and not c2:
                new = ListNode(c1.val)
                c1 = c1.next
            elif c2 and not c1:
                new = ListNode(c2.val)
                c2 = c2.next
            elif c1.val <= c2.val:
                new = ListNode(c1.val)
                c1 = c1.next
            else:
                new = ListNode(c2.val)
                c2 = c2.next

            if head is None:
                head = new

            if previous:
                previous.next = new

            previous = new
        return head
