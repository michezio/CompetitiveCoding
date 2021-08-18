#include <iostream>

using namespace std;

int main() {

    int TEST;
    cin >> TEST;

    for (int i=0; i<TEST; ++i) {
        int num;
        cin >> num;

        if (num == 1) {
            cout << 1 << " " << 1 << endl;
            continue;
        }

        int pisp = num-1;
        int base = 2;
        int incr = 3;
        int ring = 2;
        while (pisp > incr) {
            pisp -= incr;
            base += incr;
            incr += 2;
            ring += 1;

            //cout << "PISP: " << pisp << " BASE: " << base << " RING: " << ring << " INCR: " << incr << endl;
        }

        int row, col; 

        if (pisp <= ring) {
            col = ring;
            row = pisp;
        }
        else {
            row = ring;
            col = 2 * ring - pisp;
        }

        cout << row << " " << col << endl;
    }

    return 0;
}