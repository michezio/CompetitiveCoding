class Solution:
    def maxProfit(self, prices):
        total_profit = 0
        for d in range(len(prices)-1):
            total_profit += max(0, prices[d+1]-prices[d])
        return total_profit


''' C++ SOLUTION
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.size() == 0) return 0;
        int top = 0;
        for (int i=0; i<prices.size()-1; ++i) {
            top += max(0, prices[i+1]-prices[i]);
        }
        return top;
    }
};
'''
