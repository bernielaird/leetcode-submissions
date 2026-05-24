class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]
        while l <= r:
            temp = (l + r) // 2
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            res = min(res, nums[temp])
            if nums[temp] < nums[r]:
                r = temp - 1
            elif nums[l] <= nums[temp]:
                l = temp + 1

        return res