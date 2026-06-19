# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        ln = 0
        i = 0
        while curr:
            ln += 1
            curr = curr.next
        remove = ln - n
        if remove == 0: return head.next
        curr = head
        for i in range(ln - 1):
            if i + 1 == remove:
                curr.next = curr.next.next
                break
            curr = curr.next
        return head