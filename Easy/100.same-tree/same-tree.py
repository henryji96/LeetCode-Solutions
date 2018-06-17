# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        self.same = True
        self.postOrder(p, q)

        return self.same

    def postOrder(self, p, q):
        if not q  and not p:
            return
        elif (not p) or (not q):
            self.same = False
            return

        if(p.val != q.val):
            self.same = False

        self.postOrder(p.left, q.left)
        self.postOrder(p.right, q.right)
