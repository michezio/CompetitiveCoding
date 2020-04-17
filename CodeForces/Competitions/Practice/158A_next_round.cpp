// https://codeforces.com/problemset/problem/158/A
// 158A Next Round

#include <stdio.h>

using namespace std;

int main()
{
    int n, k;
    scanf("%d%d", &n, &k);
    int scores[n];
    for (int i=0; i<n; i++)
        scanf("%d", &scores[i]);

    

    int i = 0;
    int counter = 0;
    if (k >= n) 
        while(i < n && scores[i++] > 0)
            counter++;
    else
        while(i < n && scores[i] >= scores[k-1] && scores[i++] > 0)
            counter++;
    
    printf("%d", counter);
}