# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        prev = None
        while head:
            cur = head
            head = head.next
            cur.next = prev
            prev = cur

        return cur




class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        valList = []
        while head:
            valList.append(head.val)
            head = head.next


        newHead = None

        for v in valList[::-1]:
            if not newHead:
                newHead = ListNode(v)
                ans = newHead
                continue
            newHead.next = ListNode(v)
            newHead = newHead.next

        return ans
