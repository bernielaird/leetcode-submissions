class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        resDict = {}
        for i in nums:
            resDict[i] = resDict.get(i, 0) + 1
        sortedKeys = sorted(resDict, key=resDict.get, reverse=True)
        return sortedKeys[:k]