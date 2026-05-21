class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        numsSorted = sorted(nums)
        for i in range(len(numsSorted)):
            l, r = i + 1, len(nums) - 1
            while l < r:
                temp = numsSorted[l] + numsSorted[r]
                target = 0 - numsSorted[i]
                if (temp == target) and ((l != i) and (r != i)):
                    resArray = tuple(sorted([numsSorted[l],numsSorted[r],numsSorted[i]]))
                    if resArray not in res:
                        res.add(resArray)
                if (temp < target) or (l == i):
                    l += 1
                else:
                    r -= 1
        return [list(x) for x in res]
            