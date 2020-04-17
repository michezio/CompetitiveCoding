class MinStack:

    def __init__(self):
        self.struct = []
        self.minimum = []

    def push(self, x):
        self.struct.append(x)
        if len(self.minimum) == 0:
            self.minimum.append(x)
        else:
            self.minimum.append(min(self.minimum[-1], x))

    def pop(self) -> None:
        self.struct.pop()
        self.minimum.pop()

    def top(self) -> int:
        return self.struct[-1]

    def getMin(self) -> int:
        return self.minimum[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

'''
C++ CODE
class MinStack {
private:
    stack<pair<int, int>> s;
public:
    /** initialize your data structure here. */

    MinStack() {
    }

    void push(int x) {
        if (s.size() == 0) s.push(make_pair(x, x));
        else s.push(make_pair(x, min(x, s.top().second)));
    }

    void pop() {
        s.pop();
    }

    int top() {
        return s.top().first;
    }

    int getMin() {
        return s.top().second;
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(x);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
'''
