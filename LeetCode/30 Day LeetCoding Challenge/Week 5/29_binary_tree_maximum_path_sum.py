# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        max_sum = 0
        max_el = float("-inf")

        def maxSubSum(node):
            nonlocal max_sum, max_el
            if node is None:
                return 0
            elif node.left is None and node.right is None:
                max_el = max(max_el, node.val)
                return max(0, node.val)
            else:
                max_el = max(max_el, node.val)
                left = maxSubSum(node.left)
                right = maxSubSum(node.right)
                max_sum = max(max_sum, left + right + node.val)
                return max(0, max(left, right) + node.val)

        maxSubSum(root)
        return max(max_sum, max_el) if max_sum != 0 else max_el
