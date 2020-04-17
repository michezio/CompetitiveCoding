// https://codeforces.com/problemset/problem/579/B
// 579B Finding Team Member

// not working yet

#include <iostream>
#include <vector>

using namespace std;

#define INPUT(x) long long (x); scanf("%lld", &(x))

typedef long long ll;

const ll INF = 10e6 + 5;
const ll TAKEN = 401;

pair<int,int> findLessZero(int r[], int c[], int size)
{
    pair<int,int> designated(-1,-1);
    int min_row = size, min_col = size;
    for (int i=0; i<size; ++i)
    {
        if (r[i] < min_row) 
        {
            min_row = r[i];
            designated.first = i;
        }
        if (c[i] < min_col)
        {
            min_col = c[i];
            designated.second = i;
        }
    }
    if (min(designated.first, designated.second) == designated.first)
        return make_pair(designated.first, -1);
    else
        return make_pair(-1, designated.second);
}

int main()
{
    INPUT(people);
    people *= 2;

    ll scores[people][people];
    int person[people];
    int rows[people], cols[people];

    for (int i=0; i<people; ++i)
        rows[i] = cols[i] = 0;

    for (int y=0; y<people; ++y)
    {
        scores[y][y] = INF;
        for (int x=y+1; x<people; ++x)
        {
            INPUT(score);
            scores[y][x] = scores[x][y] = INF - score;
        }
    }

    for (int r=0; r<people; ++r)
    {
        if (!rows[r])
        {
            ll min = INF;
            for (int c=0; c<people; ++c)
                if (scores[r][c] <= min) min = scores[r][c];
            for (int c=0; c<people; ++c)
            {
                if ((scores[r][c] -= min) == 0)
                {
                    rows[r]++;
                    cols[c]++;
                }
                    
            }
                
        }
    }
    for (int c=0; c<people; ++c)
    {
        if (!cols[c])
        {
            ll min = INF;
            for (int r=0; r<people; ++r)
                if (scores[r][c] <= min) min = scores[r][c];
            for (int r=0; r<people; ++r)
            {
                if ((scores[r][c] -= min) == 0)
                {
                    rows[r]++;
                    cols[c]++;
                }
                    
            }
        }
    }

    int teams_formed = 0;

    while(teams_formed < people)
    {
        auto found = findLessZero(rows, cols, people);

        for (int i=0; i<people; ++i)
        {
            if (found.first >= 0) 
            {
                if (scores[found.first][i] == 0)
                {
                    rows[found.first] = cols[i] = TAKEN;
                    rows[i] = cols[found.first] = TAKEN;
                    person[found.first] = i;
                    person[i] = found.first;
                    teams_formed++;
                    break;
                } 
            }
            else
            {
                if (scores[i][found.second] == 0)
                {
                    rows[found.second] = cols[i] = TAKEN;
                    rows[i] = cols[found.second] = TAKEN;
                    person[found.second] = i;
                    person[i] = found.second;
                    teams_formed++;
                    break;
                }
            }
        }
    }
    
    for (int i=0; i<people; ++i)
    {
        printf("%d ", person[i]+1);
    }
}