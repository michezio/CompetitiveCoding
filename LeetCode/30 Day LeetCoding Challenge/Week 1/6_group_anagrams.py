class Solution:
    def groupAnagrams(self, strs):
        groups = {}
        for w in strs:
            index = "".join(sorted(list(w)))
            if index in groups:
                groups[index].append(w)
            else:
                groups[index] = [w]
        return [x[1] for x in groups.items()]
