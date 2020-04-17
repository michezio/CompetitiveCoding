// https://codeforces.com/problemset/problem/492/B
// 492B Vanya and Lanterns

#include <iostream>
#include <set>
#include <vector>

using namespace std;

#define ll long long

int main()
{
    ll n, len;
    cin >> n >> len;

    set<ll> lants;

    for (ll i=0; i<n; ++i)
    {
        ll x;
        cin >> x;
        lants.insert(x);
    }

    vector<ll> lvec(lants.begin(), lants.end());

    double max_dist = lvec[0] - 0;
    for (ll i=0; i<lvec.size()-1; ++i)
    {
        double dist = (lvec[i+1] - lvec[i]) / 2.0;
        if (dist > max_dist)
            max_dist = dist; 
    }
    double dist = len - lvec[lvec.size() - 1];
    if (dist > max_dist)
        max_dist = dist;

    cout << fixed << max_dist;
}