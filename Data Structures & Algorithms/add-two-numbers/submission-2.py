# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        ans = res
        carry = 0
        while l1 or l2:
            if not l1:
                sm = l2.val + carry
                l2 = l2.next
            elif not l2:
                sm = l1.val + carry
                l1 = l1.next
            else:
                sm = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            if sm >= 10: 
                carry = 1
                sm -= 10
            else:
                carry = 0
            ans.val = sm
            if l1 or l2 or carry: ans.next = ListNode()
            ans = ans.next
        if carry: ans.val = carry
        return res