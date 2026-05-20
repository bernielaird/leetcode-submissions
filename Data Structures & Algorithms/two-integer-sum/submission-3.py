class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numSet = set()
        for i in nums:
            numSet.add(i)
        
        for i in range(len(nums)):
            if (target - nums[i]) in numSet:
                for j in range(len(nums)):
                    if (nums[j] == (target - nums[i])) and i != j:
                        return [i, j]