class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if not head:
            return None

        stack = []
        current = head

        while current:
            stack.append(current)
            current = current.next

        current = None
        reversed = None

        while stack:
            if not current:
                current = stack.pop()
                reversed = current
            else:
                current.next = stack.pop()
                current = current.next

        current.next = None
        return reversed


# Added 07/Jul/2021. Simpler iterative solution.
class Solution2:
    def reverseList(self, head: ListNode) -> ListNode:
        previous = None
        current = head
        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next
        return previous
