# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        p = head
        valList = []

        while p:
            valList.append(p.val)
            p = p.next

        return self.palindrome(valList)

    def palindrome(self, valList):
        high = len(valList) - 1
        low = 0
        while high >= low:
            if valList[low] != valList[high]:
                return False
            high -= 1
            low += 1
        return True
