# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        dx = None
        dy = None
        px = None
        py = None

        def subdepth(node, depth, parent=0):
            if node is None:
                return
            nonlocal dx, dy, px, py
            if node.val == x:
                dx = depth
                px = parent
            elif node.val == y:
                dy = depth
                py = parent
            if dx and dy:
                return
            subdepth(node.left, depth+1, node.val)
            subdepth(node.right, depth+1, node.val)

        subdepth(root, 0)
        return (dx == dy and px != py)
