# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = ""
        num2 = ""

        while l1:
            num1 += str(l1.val)
            l1 = l1.next
        while l2:
            num2 += str(l2.val)
            l2 = l2.next


        ansNum = int(num1[::-1])+int(num2[::-1])
        p = None

        if ansNum == 0:
            return ListNode(0)

        while ansNum != 0:
            curVal = ansNum % 10
            ansNum = ansNum // 10
            if p is None:
                p = ListNode(curVal)
                ansRoot = p
            else:
                p.next = ListNode(curVal)
                p = p.next

        return ansRoot
