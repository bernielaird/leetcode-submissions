# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None

        # Find Length
        dummy, length = head, 0
        while dummy:
            dummy = dummy.next
            length += 1

        prev, curr = None, head
        for i in range(length - n):
            temp = prev
            prev = curr
            curr = curr.next
        if not prev:
            head = head.next
        else:
            prev.next = curr.next
        return head