class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res, resolve_set = defaultdict(list), set()
        for item in strs:
            count = [0] * 26 #There are 26 lowercase letters
            for c in item: # For every character in item
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(item)
        return list(res.values())

            
