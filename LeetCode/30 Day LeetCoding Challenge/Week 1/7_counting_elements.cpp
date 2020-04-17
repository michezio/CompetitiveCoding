#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
    int countElements(vector<int>& arr) {
        int count = 0;
        sort(arr.begin(), arr.end());
        for (int i=0; i<arr.size()-1; ++i) {
            for (int j=i+1; j<arr.size(); ++j) {
                if (arr[j] == arr[i]+1) {
                    count++;
                    break;
                }
                else if (arr[j] - arr[i] > 1) {
                    break;
                }
            }
        }
        return count;
    }
};