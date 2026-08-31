# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def _print(self, root):
        arr = []
        while root:
            arr.append(root.val)
            root = root.next
        print(arr)

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import random
        root = None
        queue = []
        for node in lists:
            if node: queue.append((node.val, random.random(), node))
        if not queue: return None
        heapq.heapify(queue)
        while queue:
            val, _, node = heapq.heappop(queue)
            if not root: 
                root = ListNode(val)
                curr = root
            else:
                curr.val = val
            curr.next = ListNode() if queue or node.next else None
            curr = curr.next 
            node = node.next
            if not node: continue
            heapq.heappush(queue, (node.val, random.random(), node))
        # curr = None
        # self._print(root)
        return root 