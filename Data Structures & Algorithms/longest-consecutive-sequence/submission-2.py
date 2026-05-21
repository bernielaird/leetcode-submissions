class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        tempSet = set()
        for i in nums:
            tempSet.add(i)
        res = set()
        for i in nums:
            j = i
            count = 1
            while (j + 1) in tempSet:
                j += 1
                count += 1
            res.add(count)
        if res:
            return max(res)
        return 0