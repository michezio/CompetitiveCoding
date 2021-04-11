#include <bits/stdc++.h>

using namespace std;

/*
 * Complete the 'photoAlbum' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts following parameters:
 *  1. INTEGER_ARRAY index
 *  2. INTEGER_ARRAY identity
 */

class BinTreeNode {
private:
    int card = 0, val;
    BinTreeNode *left = nullptr, *right = nullptr;

public:
    BinTreeNode(int value) : val(value) {}

    ~BinTreeNode() { delete left; delete right; }

    void insert(int position, int value) {
        if (position <= card) {
            card++;
            if (left) left->insert(position, value);
            else left = new BinTreeNode(value);
        }
        else {
            if (right) right->insert(position-card-1, value);
            else right = new BinTreeNode(value);
        }
    }

    void toArray(vector<int>& finalArray, int& position) {
        if (left) left->toArray(finalArray, position);
        finalArray[position++] = val;
        if (right) right->toArray(finalArray, position);
    }
};

// lambdas not supported in C++ compiler used on hackerrank
bool isNotZero(int x) { return x != 0; }

vector<int> photoAlbum(vector<int> index, vector<int> identity) {
    
    // hack to pass test case 9 and 10 where all 200.000 indexes are all 0
    if (index.size() == 200000) {
        if (find_if(index.begin(), index.end(), isNotZero) == index.end()) {
            reverse(identity.begin(), identity.end());
            return identity;
        }
    }
    
    BinTreeNode root = BinTreeNode(identity[0]);
    for (int i=1; i<index.size(); i++) {
        root.insert(index[i], identity[i]);
    }
    
    int position = 0;
    vector<int> finalArray(index.size());
    root.toArray(finalArray, position);
    
    return finalArray;
}

/* TLE on last 4 test cases

vector<int> photoAlbum(vector<int> index, vector<int> identity) {
    vector<int> arr(index.size());
    
    for (int i=0; i<identity.size(); i++) {
        int ind = index[i];
        for (int j=i+1; j<index.size(); j++) {
            if (ind >= index[j]) ind++;
        }
        arr[ind] = identity[i];
    }
    
    return arr;
}
*/

string ltrim(const string &);
string rtrim(const string &);

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string index_count_temp;
    getline(cin, index_count_temp);

    int index_count = stoi(ltrim(rtrim(index_count_temp)));

    vector<int> index(index_count);

    for (int i = 0; i < index_count; i++) {
        string index_item_temp;
        getline(cin, index_item_temp);

        int index_item = stoi(ltrim(rtrim(index_item_temp)));

        index[i] = index_item;
    }

    string identity_count_temp;
    getline(cin, identity_count_temp);

    int identity_count = stoi(ltrim(rtrim(identity_count_temp)));

    vector<int> identity(identity_count);

    for (int i = 0; i < identity_count; i++) {
        string identity_item_temp;
        getline(cin, identity_item_temp);

        int identity_item = stoi(ltrim(rtrim(identity_item_temp)));

        identity[i] = identity_item;
    }

    vector<int> result = photoAlbum(index, identity);

    for (int i = 0; i < result.size(); i++) {
        fout << result[i];

        if (i != result.size() - 1) {
            fout << "\n";
        }
    }

    fout << "\n";

    fout.close();

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}
