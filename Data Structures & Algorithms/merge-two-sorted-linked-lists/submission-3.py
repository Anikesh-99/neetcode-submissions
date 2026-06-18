# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, curr2 = list1, list2
        if not curr1 and not curr2: return  None
        lst = ListNode()
        curr = lst
        while curr1 or curr2:
            if not curr2:
                curr.val = curr1.val
                curr1 = curr1.next
                curr.next = ListNode() if curr1 else None
            elif not curr1:
                curr.val = curr2.val
                curr2 = curr2.next
                curr.next = ListNode() if curr2 else None
            elif curr1.val >= curr2.val:
                curr.val = curr2.val
                curr2 = curr2.next
                curr.next = ListNode() if curr2 or curr1 else None
            else:
                curr.val = curr1.val
                curr1 = curr1.next
                curr.next = ListNode() if curr1 or curr2 else None
            curr = curr.next
        curr = None
        return lst
