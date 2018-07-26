class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s and not t:
            return True
        elif not s or not t:
            return False

        return self.isSameTree(s, t) or self.isSubtree(s.left,t) or self.isSubtree(s.right,t)


    def isSameTree(self, l, r):
        if not l and not r:
            return True
        elif not l or not r:
            return False
        else:
            return l.val == r.val and self.isSameTree(l.left,r.left) and self.isSameTree(l.right,r.right)
