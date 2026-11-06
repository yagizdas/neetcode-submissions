from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counted_nums = Counter(nums)
        heap, final_list = [], []
        for item, freq in counted_nums.items():
            heapq.heappush(heap, (-freq, item))
        for i in range(k):
            final_list.append(heapq.heappop(heap)[1])
        return final_list
