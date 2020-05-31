'''
FASTEST SOLUTION (100%)
'''


class Solution:
    def findAnagrams(self, string: str, match: str) -> list[int]:
        indexes = []

        import collections
        p = collections.defaultdict(int)
        for x in match:
            p[x] += 1

        def findAnagrams(first, string):
            nonlocal match, p, indexes
            end = len(string)-len(match)
            previous_anagram = False
            for i in range(end+1):
                if previous_anagram:
                    if string[i-1] == string[i+len(match)-1]:
                        indexes.append(i+first)
                    else:    
                        previous_anagram = False
                    continue
                m = p.copy()
                valid = True
                for k in string[i:i+len(match)]:
                    if m[k] == 0:
                        valid = False
                        break
                    else:
                        m[k] -= 1
                if valid:       
                    indexes.append(i+first)
                    previous_anagram = True

        letters = set(match)
        first_index = None
        last_index = None
        for i in range(len(string)):
            if string[i] in letters:
                if first_index is None:
                    first_index = i
                continue
            else:
                if first_index is None:
                    continue
                elif i - first_index >= len(match):
                    last_index = i
                    findAnagrams(first_index, string[first_index:last_index])
                    first_index = None
                    last_index = None 
        if first_index is not None and last_index is None:
            findAnagrams(first_index, string[first_index:])
        return indexes
