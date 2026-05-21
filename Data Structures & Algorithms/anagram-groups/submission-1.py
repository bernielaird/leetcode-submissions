class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resDict = defaultdict(list)
        for i in strs:
            temp = tuple(sorted(i))
            resDict[temp].append(i)
        return list(resDict.values())