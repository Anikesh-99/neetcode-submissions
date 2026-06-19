# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next or not head.next.next: return False
        fast = head.next.next
        slow = head.next
        while fast != slow:
            if not fast.next or not fast.next.next: return False
            fast = fast.next.next
            slow = slow.next
        return fast == slow