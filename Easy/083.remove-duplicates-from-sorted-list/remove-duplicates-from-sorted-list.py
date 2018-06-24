# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        elif not head.next:
            return head

        p1 = head.next
        p0 = head
        while p1:
            if p1.val != p0.val:
                p0 = p1
                p1 = p1.next
            else:
                p0.next = p1.next
                p1 = p0.next
        return head
