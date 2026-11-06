class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        count = Counter(nums)
        #buckets = [[] for _ in range(len(nums) + 1)]
        buckets = [] 
        for _ in range(len(nums)+ 1):
            buckets.append([])
        for num, freq in count.items():
            buckets[freq].append(num) #freqth bucket'a num ekliyoruz.

        res = []
        for freq in range(len(buckets) - 1, 0, -1): # iterating from highest frequency entries to lowest.
            for num in buckets[freq]:
                res.append(num)
                if len(res) == k:
                    return res

