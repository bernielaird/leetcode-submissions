# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp = 0
        res = l1
        prev = None
        # Merge l1 and l2 into l1
        while l1:
            if l2:
                val = l1.val + l2.val + temp
                l2 = l2.next
            else:
                val = l1.val + temp
            temp = 0
            if val > 9:
                l1.val = (val - 10)
                temp = 1
            else:
                l1.val = val
            prev = l1
            l1 = l1.next
                

        # Append extra l2
        while l2:
            l2.val = l2.val + temp
            if l2.val == 10:
                l2.val = 0
            else:
                temp = 0
            prev.next = l2
            prev = prev.next
            l2 = l2.next

        # Check if temp still there
        if temp == 1 and not l1:
            prev.next = ListNode(1)
        return res