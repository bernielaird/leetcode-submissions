class TimeMap:

    def __init__(self):
        self.temp = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.temp:
            self.temp[key] = []

        self.temp[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key not in self.temp:
            return res
        fun = self.temp[key]
        l, r = 0, len(fun) - 1
        
        while l <= r:
            m = (l + r) // 2
            if fun[m][0] == timestamp:
                return fun[m][1]
            if fun[m][0] > timestamp:
                r = m - 1
            else:
                res = fun[m][1]
                l = m + 1
        return res