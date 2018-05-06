# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p = ListNode(0)
        ptemp = p
        
        while(l1 != None and l2 != None):
            if(l1.val < l2.val):
                ptemp.next = l1
                l1 = l1.next
            else:
                ptemp.next = l2
                l2 = l2.next
            ptemp = ptemp.next
            
            
        if(l1 != None):
            ptemp.next = l1
        else:
            ptemp.next = l2
            
        return p.next
        