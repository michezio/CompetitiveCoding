//  https://codeforces.com/problemset/problem/1/A
//  1A Theatre Square

#include <stdio.h>
#include <math.h>

using namespace std;

int main()
{
    long long n, m, a;
    scanf("%lld%lld%lld", &n, &m, &a);

    long long w = ceil((double)n/a);
    long long h = ceil((double)m/a);

    long long total = w * h;

    printf("%lld", total);
}