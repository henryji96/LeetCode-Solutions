# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):

        if not root:
            return True

        def dfs(left, right):

            if not left and not right:
                return True
            elif not left or not right:
                return False
            elif left.val != right.val:
                return False

            return dfs(left.left,right.right) and dfs(left.right,right.left)

        return dfs(root.left,root.right)

    def isSymmetric2(self, root):
        if not root:
            return True

        stack = [root.left, root.right]
        while stack:
            t1 = stack.pop()
            t2 = stack.pop()
            if not t1 and not t2: continue
            if not t1 or not t2:  return False
            if t1.val != t2.val:  return False
            stack.append(t1.left)
            stack.append(t2.right)
            stack.append(t1.right)
            stack.append(t2.left)
        return True
