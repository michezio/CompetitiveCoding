class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class LRUCache:
    def __init__(self, capacity: int):
        self.hm = {}
        self.ls = []
        self.cap = capacity

    def get(self, key: int) -> int:
        if key in self.hm.keys():
            el = self.hm[key]
            self.ls.remove(el)
            self.ls.append(el)
            return el.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hm.keys():
            el = self.hm[key]
            self.ls.remove(el)
            el.value = value
            self.ls.append(el)
        else:
            if len(self.ls) == self.cap:
                el = self.ls.pop(0)
                del self.hm[el.key]
            self.ls.append(Node(key, value))
            self.hm[key] = self.ls[-1]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
