class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = set()
        for i,num in enumerate(nums):
            a.add(num)
            if len(a) != i+1:
                return True

        return False
            