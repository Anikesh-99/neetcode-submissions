# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        fast = head
        i = 0
        while fast and i < n:
            i += 1
            fast = fast.next
        if not fast: 
            return head.next
        while fast and fast.next:
            fast = fast.next
            curr = curr.next
        curr.next = curr.next.next if curr.next else None
        return head
