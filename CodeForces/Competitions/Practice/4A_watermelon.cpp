//  https://codeforces.com/problemset/problem/4/A
//  4A Watermelon

#include <stdio.h>

using namespace std;

int main()
{
    int w;
    scanf("%d", &w);
    if (w % 2 == 0 && w > 2) printf("YES");
    else printf("NO");
    return 0;
}
