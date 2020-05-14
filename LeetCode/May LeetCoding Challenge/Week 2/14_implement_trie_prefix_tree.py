class Trie:

    def __init__(self):
        self.letter = [None for _ in range(27)]

    def insert(self, word: str) -> None:
        root = self.letter
        for x in word:
            ind = ord(x)-97
            if root[ind] is None:
                root[ind] = [None for _ in range(27)]
            root = root[ind]
        root[-1] = True

    def search(self, word: str) -> bool:
        root = self.letter
        for x in word:
            ind = ord(x)-97
            if root[ind]:
                root = root[ind]
            else:
                return False
        return root[-1] is True

    def startsWith(self, prefix: str) -> bool:
        root = self.letter
        for x in prefix:
            ind = ord(x)-97
            if root[ind]:
                root = root[ind]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
