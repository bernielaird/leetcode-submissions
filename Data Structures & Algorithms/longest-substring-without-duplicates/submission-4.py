class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if (len(s) == 0) or (len(s) == 1):
            return len(s)
        l, r = 0, 0
        res = 0
        val = 0
        temp = set()
        while r < len(s):
            while s[r] in temp:
                temp.remove(s[l])
                val -= 1
                l += 1
            else: 
                val += 1
            temp.add(s[r])
            res = max(res, val)
            r += 1
        return res