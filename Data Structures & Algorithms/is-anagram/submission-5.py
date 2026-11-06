class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        counts = {}
        for item in s:
            counts[item] = counts.get(item, 0) + 1
        for item in t:
            counts[item] = counts.get(item, 0) - 1
            if counts[item] < 0: return False
        return True