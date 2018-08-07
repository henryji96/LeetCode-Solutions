# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """

        # compute len of linked list
        lenth = 0
        p = root
        while p:
            lenth += 1
            p = p.next

        # determine the length of each part
        part_size = lenth // k
        longer_part_num = lenth % k
        ans = [part_size+1] * longer_part_num  + [part_size] * (k-longer_part_num)

        # split up linked list
        prev, head = None, root
        for i, num in enumerate(ans):
            ans[i] = head
            for j in range(num):
                prev, head = head, head.next

            if prev:
                prev.next = None

        return ans







        
