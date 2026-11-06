class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Creating the target dic
        targets = {}
        for i in range(len(nums)):
            targets[target - nums[i]] = i+1
        for j,num in enumerate(nums):
            b = targets.get(num, 0)
            if b > 0 and b-1 != j: 
                return[j, b-1]
                
        print(targets)