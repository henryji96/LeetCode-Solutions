# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return None

        oddHead = head
        oddP = oddHead
        evenHead = head.next
        evenP = evenHead

        while evenP and evenP.next:
            oddP.next = oddP.next.next
            oddP = oddP.next

            evenP.next = evenP.next.next
            evenP = evenP.next

        oddP.next = evenHead

        return oddHead
