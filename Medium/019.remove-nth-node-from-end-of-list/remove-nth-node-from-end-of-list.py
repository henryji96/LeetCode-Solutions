# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        size = self.getSize(head)
        dummy = ListNode(0)
        dummy.next = head

        p = dummy
        for i in range(size - n):
            p = p.next
        p.next = p.next.next

        return dummy.next


    def getSize(self, node):
        ans = 0
        while node:
            node = node.next
            ans += 1
        return ans
