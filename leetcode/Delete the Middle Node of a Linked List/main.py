# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def from_list(cls, l: list[int]) -> "ListNode | None":
        head = None
        current = None

        for val in l:
            if head is None:
                head = cls(val)
                current = head
            else:
                current.next = cls(val)
                current = current.next

        return head

    def as_list(self):
        l = []
        current = self
        while current:
            l.append(current.val)
            current = current.next
        return l


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        # calculate size of the list
        n = 0
        current = head
        while current:
            n += 1
            current = current.next

        # get the middle idx
        middle_idx = n // 2
        if middle_idx == 0:
            return None

        n = 0
        previous = None
        current = head

        # find the element to delete
        while current:
            if n == middle_idx:
                break

            previous = current
            current = current.next
            n += 1

        # handle previous element
        if previous:
            previous.next = current.next

        return head



if __name__ == "__main__":
    # empty list
    assert Solution().deleteMiddle(None) == None

    # single node
    assert Solution().deleteMiddle(ListNode(1)) == None

    # leetcode tests
    original = ListNode.from_list([1,3,4,7,1,2,6])
    print(f"{original.as_list()=}")
    modified = Solution().deleteMiddle(original)
    print(f"{modified.as_list()=}")
    assert modified.as_list() == [1,3,4,1,2,6]

    original = ListNode.from_list([1, 2, 3, 4])
    print(f"{original.as_list()=}")
    modified = Solution().deleteMiddle(original)
    print(f"{modified.as_list()=}")
    assert modified.as_list() == [1, 2, 4]

    original = ListNode.from_list([2, 1])
    print(f"{original.as_list()=}")
    modified = Solution().deleteMiddle(original)
    print(f"{modified.as_list()=}")
    assert modified.as_list() == [2]
