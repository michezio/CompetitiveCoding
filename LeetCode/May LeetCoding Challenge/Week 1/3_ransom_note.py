class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = dict.fromkeys((chr(x+97) for x in range(26)), 0)
        for m in magazine:
            d[m] += 1
        for c in ransomNote:
            if d[c] == 0:
                return False
            else:
                d[c] -= 1
        return True


''' C++ CODE
class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        unordered_map<char,int> cnt;
        for (char c : magazine)
            cnt[c]++;
        for (char c : ransomNote) {
            if (--cnt[c] < 0)
                return false;
        }
        return true;
    }
};
'''
