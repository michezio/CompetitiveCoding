# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def diameterOfBinaryTree(self, root):
        self.dp = {}

        def height(subtree):
            if subtree is None:
                return 0
            if subtree.left not in self.dp.keys():
                self.dp[subtree.left] = height(subtree.left)
            if subtree.right not in self.dp.keys():
                self.dp[subtree.right] = height(subtree.right)
            lh = self.dp[subtree.left]
            rh = self.dp[subtree.right]
            return 1 + max(lh, rh)

        def diameter(subtree):
            if subtree is None:
                return 0
            lh = height(subtree.left)
            rh = height(subtree.right)
            ld = diameter(subtree.left)
            rd = diameter(subtree.right)
            return max(lh + rh, max(ld, rd))

        return diameter(root)
