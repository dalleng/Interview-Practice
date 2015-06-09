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
