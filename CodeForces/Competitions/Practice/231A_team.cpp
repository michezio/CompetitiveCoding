// https://codeforces.com/problemset/problem/231/A
// 231A Team

#include <string>
#include <iostream>

using namespace std;

int main()
{
    int counter = 0;

    int w;
    cin >> w;

    while(w--)
    {
        int a, b, c;
        cin >> a >> b >> c;

        counter += (a+b+c) >= 2 ? 1 : 0;
    }

    cout << counter;
}