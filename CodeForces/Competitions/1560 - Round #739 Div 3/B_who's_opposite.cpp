#include <iostream>

using namespace std;

int main() {

    int TEST;
    cin >> TEST;

    for (int i=0; i<TEST; ++i) {
        int a,b,c;
        cin >> a >> b >> c;

        int midv = max(a, b) - min(a, b) + 1;
        int maxv = midv * 2 - 2;

        if (abs(a-b) < min(a, b) || c > maxv) {
            cout << -1 << endl;
        }
        else {
            int opp = 1 + c-midv;
            if (opp <= 0) opp += maxv;
            cout << opp << endl;
        }
    }

    return 0;
}