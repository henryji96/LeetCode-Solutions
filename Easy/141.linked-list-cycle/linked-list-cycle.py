# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        if not head:
            return False

        nodeSet = set()


        while head!= None:      # O(n)
            nodeSet.add(head)
            head = head.next
            if head in nodeSet:
                return True

        return False
