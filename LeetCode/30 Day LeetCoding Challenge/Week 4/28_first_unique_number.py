class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DLList:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def add(self, value):
        if self.length == 0:
            self.first = Node(value)
            self.last = self.first
        else:
            self.last.next = Node(value)
            self.last.next.prev = self.last
            self.last = self.last.next
        self.length += 1

    def remove(self, node):
        if self.first == node:
            self.first = node.next
            if node.next is not None:
                node.next.prev = None
        elif self.last == node:
            self.last = node.prev
            if node.prev is not None:
                node.prev.next = None
        else:
            if node.prev is not None:
                node.prev.next = node.next
            if node.next is not None:
                node.next.prev = node.prev
        del node
        self.length -= 1


class FirstUnique:

    def __init__(self, nums):
        self.unique = DLList()
        self.appeared = {}
        for n in nums:
            self.add(n)

    def showFirstUnique(self):
        return self.unique.first.value if self.unique.length > 0 else -1

    def add(self, n):
        if n not in self.appeared.keys():
            self.unique.add(n)
            self.appeared[n] = self.unique.last
        else:
            if self.appeared[n] is not None:
                self.unique.remove(self.appeared[n])
                self.appeared[n] = None

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
