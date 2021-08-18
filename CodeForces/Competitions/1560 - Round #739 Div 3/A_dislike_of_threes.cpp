#include <iostream>

using namespace std;

int arr[1000];

int main() {

    int pos = 0;
    for (int num=1; num<=1666; num++) {
        if (num % 3 == 0 || num % 10 == 3) continue;
        arr[pos++] = num;
    }

    int TEST;
    cin >> TEST;

    for (int i=0; i<TEST; ++i) {
        int index = 0;
        cin >> index;
        cout << arr[index-1] << endl;
    }

    return 0;
}