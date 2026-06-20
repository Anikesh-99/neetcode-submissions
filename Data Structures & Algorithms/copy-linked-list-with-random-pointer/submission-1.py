"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
import random
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return head
        ln = 0
        ans = Node(0)
        point = ans
        runner = head
        lst = []
        while runner:
            point.val = runner.val
            ln += 1
            runner = runner.next
            if runner: 
                point.next = Node(0)
                point = point.next
        runner = head
        while runner:
            point = head
            i = 0
            while point != runner.random:
                i += 1
                point = point.next
            lst.append(i)
            runner = runner.next
        point = ans
        currPos = 0
        while point:
            runner = ans
            i = 0
            while runner and lst[currPos] != i:
                i += 1
                runner = runner.next
            point.random = runner
            currPos += 1
            point = point.next
        return ans