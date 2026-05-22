class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        vals = {}
        l, r = 0, 0
        res = 0

        while r < k:
            vals[s[r]] = vals.get(s[r], 0) + 1
            r += 1
            res = max(res, (r - l))

        while r < len(s):
            vals[s[r]] = vals.get(s[r], 0) + 1
            
            while (r - l + 1) - max(vals.values()) > k:
                vals[s[l]] = vals[s[l]] - 1
                l += 1
            
            res = max(res, (r - l + 1))
            r += 1
        return res
            