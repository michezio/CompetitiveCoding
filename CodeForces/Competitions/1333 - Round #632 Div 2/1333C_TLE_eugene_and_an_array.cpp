// https://codeforces.com/problemset/problem/1333/C
// 1333C Eugene and an Array


#include <iostream>
#include <map>

#define mp make_pair

using namespace std;

int total = 0;

map<pair<int, int>, bool> dp;
long long arr[200001];

bool checkSubarray(int begin, int end) {
    auto itr = dp.find(mp(begin, end));
    if (itr != dp.end())
        return itr->second;
    else if (end-begin == 1) {
        bool isNotZero = arr[begin] != (begin > 0 ? arr[begin-1] : 0);
        dp.insert({mp(begin, end), isNotZero});
        return isNotZero;
    }
    else {
        bool res = checkSubarray(begin, end-1) && checkSubarray(begin+1, end);
        bool nres = arr[end-1] != (begin-1 < 0 ? 0 : arr[begin-1]);
        res &= nres;
        dp.insert({mp(begin,end), res});
        total += res ? 1 : 0;
        return res;
    }
}


int main() {
    
    int L;
    cin >> L;

    cin >> arr[0];
    unsigned long count = 0;
    if (arr[0] == 0) count++;
    for (int i=1; i<L; ++i) {
        cin >> arr[i];
        if (arr[i] == 0) count++;
        arr[i] += arr[i-1];
    }

    total = L - count;

    if (total == 0) {
        cout << 0;
        return 0;
    }

    auto res = checkSubarray(0, L);
    
    cout << total;
}
