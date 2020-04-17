// https://codeforces.com/problemset/problem/50/A
// 50A Domino Piling

#include <stdio.h>

using namespace std;

int main()
{
    int r, c;
    scanf("%d%d", &r, &c);

    int area = r * c;

    int pieces = area / 2;

    printf("%d", pieces);
}