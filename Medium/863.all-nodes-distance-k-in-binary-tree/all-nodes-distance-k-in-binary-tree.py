# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        self.nodeVisited = {}
        nodeNeighbor = collections.defaultdict(set)
        self.graph(root, nodeNeighbor)
        ans = []
        self.dfs(target, ans, K, nodeNeighbor)

        return ans

    def dfs(self, root, ans, K, nodeNeighbor):

        if self.nodeVisited[root]:
            self.nodeVisited[root] = False

            if K == 0:
                ans.append(root.val)
                return

            for node in nodeNeighbor[root]:
                self.dfs(node, ans, K-1, nodeNeighbor)




    def graph(self, root, nodeNeighbor):

        if root:
            self.nodeVisited[root] = True
        if root.left:
            nodeNeighbor[root].add((root.left))
            nodeNeighbor[root.left].add((root))
            self.graph(root.left, nodeNeighbor)
        if root.right:
            nodeNeighbor[root].add((root.right))
            nodeNeighbor[root.right].add((root))
            self.graph(root.right, nodeNeighbor)
