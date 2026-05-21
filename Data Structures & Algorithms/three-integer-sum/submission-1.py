class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        numsSorted = sorted(nums)
        for i in range(len(numsSorted)):
            l, r = 0, len(nums) - 1
            while l < r:
                temp = numsSorted[l] + numsSorted[r]
                target = 0 - numsSorted[i]
                if (temp == target) and ((l != i) and (r != i)):
                    resArray = sorted([numsSorted[l],numsSorted[r],numsSorted[i]])
                    if resArray not in res:
                        res.append(resArray)
                if (temp < target) or (l == i):
                    l += 1
                else:
                    r -= 1
        return res
            