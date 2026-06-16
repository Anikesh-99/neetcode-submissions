class TimeMap:

    def __init__(self):
        self.hm = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        lst = self.hm[key]
        if not lst or lst[-1][0] < timestamp: self.hm[key].append((timestamp, value))
        l, r = 0, len(lst) - 1
        while l <= r:
            m = l + (r-l)//2
            time = lst[m][0]
            if time == timestamp: break
            if time < timestamp:
                l = m + 1
            else:
                r = m - 1
        if lst[m][0] == timestamp: self.hm[key][m] = (timestamp, value)
        else: self.hm[key] = self.hm[key][:m] + [(timestamp, value)] + self.hm[key][m:]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hm or self.hm[key][0][0] > timestamp: return "" 
        if len(self.hm[key]) == 0: return self.hm[key][0][1]
        lst = self.hm[key]
        l, r = 0, len(lst) - 1
        while l <= r:
            m = l + (r-l)//2
            time = lst[m][0]
            if time == timestamp: break
            if time < timestamp:
                l = m + 1
            else:
                r = m - 1
        # print(self.hm[key], timestamp, m)
        time = self.hm[key][m][0]
        if time <= timestamp or m == 0: return self.hm[key][m][1]
        return self.hm[key][m - 1][1]
