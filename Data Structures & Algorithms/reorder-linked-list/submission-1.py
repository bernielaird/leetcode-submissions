# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Seperate into halves.
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half of linked list.
        dummy = slow.next
        prev = slow.next = None
        while dummy:
            temp = dummy.next
            dummy.next = prev
            prev = dummy
            dummy = temp

        # Merge the linked lists.
        curr = head
        while prev:
            temp1 = curr.next
            curr.next = prev
            curr = temp1

            temp2 = prev.next
            prev.next = curr
            prev = temp2

