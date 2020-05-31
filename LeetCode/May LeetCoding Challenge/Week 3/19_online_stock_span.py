class StockSpanner:

    def __init__(self):
        self.elems = []

    def next(self, price: int) -> int:

        index = len(self.elems)-1
        self.elems.append([price, 1])
        while index >= 0:
            if self.elems[index][0] > price:
                break
            else:
                shift = self.elems[index][1]
                self.elems[-1][1] += shift
                index -= shift
        return self.elems[-1][1]

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
