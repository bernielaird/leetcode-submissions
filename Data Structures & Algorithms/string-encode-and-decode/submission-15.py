class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res = res + str(len(i)) + "#" + i
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        counter = 0
        temp = ""
        for i in s:
            if counter != 0:
                tempStr = tempStr + i
                counter -= 1
                if counter == 0:
                    res.append(tempStr)
            elif i == "#" and temp != "":
                counter = int(temp)
                tempStr,temp = "",""
                if counter == 0:
                    res.append(tempStr)
            else: 
                if i.isnumeric():
                    temp = temp + i
                else:
                    i = ""
        return res
