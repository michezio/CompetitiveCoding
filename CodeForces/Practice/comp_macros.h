#include <cmath>
#include <climits>
#include <queue>
#include <vector>
#include <map>
#include <cstdlib>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <stack>
#include <algorithm>
#include <cstring>
#include <cassert>

using namespace std;

//data types used often, but you don't want to type them time by time
#define LL long long
#define ULL unsigned long long
#define UI unsigned int
#define US unsigned short
#define IOS ios_base::sync_with_stdio(0); //to synchronize the input of cin and scanf
#define INF 1001001001
#define PI 3.1415926535897932384626

#define BIT(x, i) (x & (1 << i)) //select the bit of position i of x
#define LBIT(x) ((x) & ((x) ^ ((x)-1))) //get the lowest bit of x
#define HBIT(msb, n) asm("bsrl %1,%0" : "=r"(msb) : "r"(n)) //get the highest bit of x, maybe the fastest

#define MAX(a, b) (a < b ? b : a)
#define ABS(x) (x < 0 ? (-x) : x) // big bug here if "-x" is not surrounded by "()"
#define EVEN(x) (x % 2 == 0)
#define ODD(x) (x % 2 != 0)

//the next for are for checking bound
#define IN(i, l, r) (l < i && i < r) 
#define LINR(i, l, r) (l <= i && i <= r)
#define LIN(i, l, r) (l <= i && i < r)
#define INR(i, l, r) (l < i && i <= r)

//next four are for "for loops"
#define F(i, L, R) for (LL i = L; i < R; i++)
#define FE(i, L, R) for (LL i = L; i <= R; i++)
#define FF(i, L, R) for (LL i = L; i > R; i--)
#define FFE(i, L, R) for (LL i = L; i >= R; i--)

//next three are handy ways to get ints, it's also force you to use '&' sign
#define GET1(a) scanf("%d", &a) 
#define GET2(a, b) scanf("%d%d", &a, &b)
#define GET3(a, b, c) scanf("%d%d%d", &a, &b, &c)
#define GETS(x) scanf("%s", x) //get a char* string
#define INIT1(n) LL (n); scanf("%lld", &(n)) 
#define INIT2(n, m) LL (n), (m); scanf("%lld%lld", &(n), &(m))
#define INIT3(n, m, k) LL (n), (m), (k); scanf("%lld%lld%lld", &(n), &(m), &(k))

//for multilple cases problems
#define TESTS wez(testow) while (testow--) 
#define WHILEZ LL T; getI(T); while (T--)

#define CLR(a, x) memset(a, x, sizeof(a)) //set elements of array to some value
#define CHAR2INT(c) (c - '0')
#define LAST(vec) vec[vec.size() - 1]
#define SIZE(x) ((LL)((x).size()))
#define REMAX(a, b) (a) = max((a), (b)) // set a to the maximum of a and b
#define REMIN(a, b) (a) = min((a), (b));
#define FOREACH(i, t) for (typeof(t.begin()) i = t.begin(); i != t.end(); i++)
#define ALL(c) (c).begin(), (c).end()
#define PRESENT(c, x) ((c).find(x) != (c).end())
#define CPRESENT(c, x) (find(ALL(c), x) != (c).end())

//for map, pair
#define mp make_pair
#define fi first
#define se second

// for debug
inline void pisz(int n) { printf("%d\n", n); }
#define DBG(vari) cerr << #vari << " = " << (vari) << endl;
#define printA(a, L, R) FE(i, L, R) cout << a[i] << (i == R ? '\n' : ' ')
#define printV(a) printA(a, 0, a.size() - 1)
#define MAXN 10000

//for vectors
#define pb push_back
#define eb emplace_back
typedef int elem_t;
typedef vector<LL> vi;
typedef vector<vi> vvi;
typedef pair<LL, LL> ii;
typedef vector<ii> vii;
typedef vector<vii> vvii;

// directions
const int fx[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
const int fxx[8][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}, {1, 1}, {1, -1}, {-1, 1}, {-1, -1}};

template <typename T, typename TT>
ostream &operator<<(ostream &s, pair<T, TT> t) { return s << "(" << t.first << "," << t.second << ")"; }
template <typename T>
ostream &operator<<(ostream &s, vector<T> t)
{
    F(i, 0, SZ(t))
        s << t[i] << " ";
    return s;
}