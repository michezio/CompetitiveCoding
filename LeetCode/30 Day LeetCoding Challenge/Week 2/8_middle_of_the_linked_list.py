# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def middleNode(self, head):
        element = head
        middle = head
        count = 0
        while (element.next is not None):
            if (count % 2 == 0):
                middle = middle.next
            element = element.next
            count += 1
        return middle
