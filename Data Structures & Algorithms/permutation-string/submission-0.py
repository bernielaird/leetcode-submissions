class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Hash = {}
        for i in s1:
            s1Hash[i] = s1Hash.get(i, 0) + 1

        l, r = 0, 0
        s2Hash = {}
        while r < len(s2):
            s2Hash[s2[r]] = s2Hash.get(s2[r], 0) + 1
            if (r - l + 1) > len(s1):
                s2Hash[s2[l]] = s2Hash[s2[l]] - 1
                if s2Hash[s2[l]] == 0:
                    s2Hash.pop(s2[l])
                l += 1
            if s2Hash == s1Hash:
                return True
            r += 1
        return False

