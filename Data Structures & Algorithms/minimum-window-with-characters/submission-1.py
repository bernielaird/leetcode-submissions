class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = s + "1"
        if len(t) > len(s):
            return ""
        tHash = {}
        sHash = {}
        for i in t:
            tHash[i] = tHash.get(i, 0) + 1
        
        l, r = 0,0
        while r < len(s):
            temp = True
            sHash[s[r]] = sHash.get(s[r], 0) + 1
            while temp:
                for j in tHash.keys():
                    if tHash[j] > sHash.get(j, 0):
                        temp = False
                print (r)
                print (temp)
                print (sHash)
                if temp:
                    if len(s[l:r]) < len(res):
                        res = s[l:r+1]
                    sHash[s[l]] = sHash[s[l]] - 1
                    if sHash[s[l]] == 0:
                        sHash.pop(s[l])
                    l += 1
            r += 1
        if res == (s + "1"):
            return ""
        return res
