class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counts_s = {}
        counts_t = {}
        for x in s:
            counts_s[x] = counts_s.get(x, 0) + 1
        for x in t:
            counts_t[x] = counts_t.get(x, 0) + 1
        return counts_s == counts_t