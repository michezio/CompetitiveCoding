# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        odd = head
        first_even = head.next
        even = head.next
        current = None if even is None else even.next
        while (current):
            odd.next = current
            even.next = None if current is None else current.next
            even = even.next
            odd = odd.next
            current = None if even is None else even.next
        odd.next = first_even
        return head
