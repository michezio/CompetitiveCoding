// https://codeforces.com/problemset/problem/579/A
// 579A Raising Bacteria

#include <iostream>
#include <bitset>

using namespace std;

int main()
{
    long long num;
    scanf("%lld", &num);

    bitset<32> bacterias(num);
    int bacteria_to_put = bacterias.count();

    printf("%d", bacteria_to_put);
}