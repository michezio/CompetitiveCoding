# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        index = 0
        result = None

        def traverse(root):
            nonlocal index, result
            if index > k:
                return    
            if root.left:
                traverse(root.left)
            index += 1
            if index == k:
                result = root.val
            if root.right:
                traverse(root.right)

        traverse(root)
        return result
