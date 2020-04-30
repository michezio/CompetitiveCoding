# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidSequence(self, root: TreeNode, arr: list[int]) -> bool:
        valid = False
        path = [root]
        i = 0
        while (i < len(arr)):
            valid = False
            n = arr[i]
            new_paths = []
            for p in path:
                if n == p.val:
                    valid = True
                    if p.left is not None:
                        new_paths.append(p.left)
                    if p.right is not None:
                        new_paths.append(p.right)
            path = new_paths
            i += 1
        return valid if len(path) == 0 else False
