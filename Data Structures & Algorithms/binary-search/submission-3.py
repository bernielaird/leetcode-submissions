class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0,len(nums) - 1
        while l <= r:
            temp = (l + r) // 2
            if nums[temp] == target:
                return temp
            if nums[temp] < target:
                l = temp + 1
            else:
                r = temp - 1
        return -1