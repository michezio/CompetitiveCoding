// https://codeforces.com/problemset/problem/118/A
// 118A String Task

#include <string>
#include <algorithm>
#include <iostream>

using namespace std;

string vowels = "aeiouy";

bool isVowel(char s)
{
    for (int i=0; i<6; i++)
        if (s == vowels[i])
            return true;
    return false;
}

int main()
{
    string s;
    cin >> s;

    string out;
    for (int i=0; i<s.size(); i++)
    {
        s[i] = tolower(s[i]);
        if (isVowel(s[i])) continue;
        out = out + "." + s[i];
    }

    cout << out;
}