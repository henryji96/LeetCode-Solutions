# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return None

        dummy = ListNode(0)
        dummy.next = head

        p1 = head
        p2 = dummy

        while p1:
            if p1.val == val:
                p2.next = p1.next
                p1 = p2.next
                if not p1:
                    break
                continue

            p2 = p1
            p1 = p1.next


        return dummy.next
