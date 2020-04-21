# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def bstFromPreorder(self, preorder):
        root = TreeNode(preorder[0])
        for x in preorder[1:]:
            last = root
            while True:
                if x < last.val:
                    if last.left is None:
                        last.left = TreeNode(x)
                        break
                    else:
                        last = last.left
                else:
                    if last.right is None:
                        last.right = TreeNode(x)
                        break
                    else:
                        last = last.right
        return root
